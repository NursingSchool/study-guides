#!/usr/bin/env python3
"""Tests for the per-class study-hub registration in assemble_quiz.py.
Run: python test_hub.py   (plain asserts, no pytest dependency)."""
import sys, json, tempfile, subprocess, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
SKILL = HERE.parent
sys.path.insert(0, str(HERE))
import assemble_quiz as A


def check(name, cond):
    print(("PASS" if cond else "FAIL"), "-", name)
    if not cond:
        raise SystemExit(f"FAILED: {name}")


# --- slugify ---
check("slugify words", A.slugify("NR327 Maternal-Child Nursing") == "nr327-maternal-child-nursing")
check("slugify punctuation", A.slugify("  Exam 2 / Review!! ") == "exam-2-review")

# --- class page: register, idempotent, ordering ---
d = pathlib.Path(tempfile.mkdtemp())
cp = d / "nr327-maternal-child.html"
A.ensure_class_page(cp, "NR327", "Maternal-Child Nursing")
A.register_on_class_page(cp, href="mc.html", exam="Exam 2", exam_order=2, kind="exam-review",
                         title="Exam 2 Review", meta_line="136 questions", chips=["Labor"])
A.register_on_class_page(cp, href="fetal.html", exam="Exam 2", exam_order=2, kind="topic-practice",
                         title="Fetal Monitoring - practice", meta_line="12 questions", chips=["EFM"])
html = cp.read_text(encoding="utf-8")
check("two cards on class page", html.count("<!-- quiz-card:") == 2)
check("exam-review before topic-practice", html.index("mc.html") < html.index("fetal.html"))
check("topic badge rendered", "Topic Practice" in html and "Exam Review" in html)

A.register_on_class_page(cp, href="mc.html", exam="Exam 2", exam_order=2, kind="exam-review",
                         title="Exam 2 Review", meta_line="140 questions", chips=["Labor"])
html = cp.read_text(encoding="utf-8")
check("card update is idempotent", html.count("<!-- quiz-card:mc.html -->") == 1)
check("card content updated", "140 questions" in html and "136 questions" not in html)

A.register_on_class_page(cp, href="ex1.html", exam="Exam 1", exam_order=1, kind="exam-review",
                         title="Exam 1 Review", meta_line="50 questions", chips=["Intro"])
html = cp.read_text(encoding="utf-8")
check("lower exam sorts before higher", html.index("ex1.html") < html.index("mc.html"))
check("download link only when set", html.count('class="dl"') == 0)
A.register_on_class_page(cp, href="dl.html", exam="Exam 1", exam_order=1, kind="topic-practice",
                         title="With download", meta_line="8 questions", chips=["x"], download="files/x.zip")
check("download link renders when set", 'class="dl"' in cp.read_text(encoding="utf-8"))

# --- hub: class cards, idempotent, count update ---
hub = d / "index.html"
A.register_class_on_hub(hub, class_slug="nr327-maternal-child", class_code="NR327",
                        class_name="Maternal-Child Nursing", class_page_href="nr327-maternal-child.html",
                        review_count=2, exam_chips=["Exam 2"])
A.register_class_on_hub(hub, class_slug="nr228-nutrition", class_code="NR228",
                        class_name="Nutrition", class_page_href="nr228-nutrition.html", review_count=1)
htxt = hub.read_text(encoding="utf-8")
check("two class cards on hub", htxt.count("<!-- class-card:") == 2)
A.register_class_on_hub(hub, class_slug="nr327-maternal-child", class_code="NR327",
                        class_name="Maternal-Child Nursing", class_page_href="nr327-maternal-child.html",
                        review_count=3)
htxt = hub.read_text(encoding="utf-8")
check("class card idempotent", htxt.count("<!-- class-card:nr327-maternal-child -->") == 1)
check("review count updated", "3 reviews" in htxt)

# --- end-to-end via the CLI (subprocess) ---
e2e = pathlib.Path(tempfile.mkdtemp())
qs = [{"n": i + 1, "topic": f"Topic{i}", "type": "radio", "cat": "Management of Care", "lvl": "Application",
       "stem": f"A nurse weighs scenario {i} and chooses the best next action here?",
       "opts": ["alpha choice", "bravo choice", "charlie choice", "delta choice"], "ans": 1,
       "rat": "because of the reasoning", "strat": "a transferable tip"} for i in range(6)]
(e2e / "q.quiz.json").write_text(json.dumps({"meta": {
    "title": "t", "header": "h", "subtitle": "s", "footnote": "f",
    "classCode": "NR327", "className": "Maternal-Child Nursing", "classSlug": "nr327-maternal-child",
    "exam": "Exam 2", "examOrder": 2, "kind": "exam-review", "cardTitle": "Exam 2 Review"},
    "questions": qs}), encoding="utf-8")
cmd = [sys.executable, str(SKILL / "scripts" / "assemble_quiz.py"), "q.quiz.json",
       "--hub", "index.html", "--template", str(SKILL / "assets" / "quiz-template.html")]
r = subprocess.run(cmd, cwd=e2e, capture_output=True, text=True)
check("e2e build exit 0", r.returncode == 0)
check("e2e class page created", (e2e / "nr327-maternal-child.html").exists())
check("e2e hub class card", "<!-- class-card:nr327-maternal-child -->" in (e2e / "index.html").read_text(encoding="utf-8"))
r2 = subprocess.run(cmd, cwd=e2e, capture_output=True, text=True)
check("e2e rerun exit 0", r2.returncode == 0)
check("e2e no duplicate card", (e2e / "nr327-maternal-child.html").read_text(encoding="utf-8").count("<!-- quiz-card:") == 1)

# --- missing class meta: warn + still build ---
nom = pathlib.Path(tempfile.mkdtemp())
(nom / "n.quiz.json").write_text(json.dumps({"meta": {"title": "t", "header": "h", "subtitle": "s", "footnote": "f"},
                                             "questions": qs}), encoding="utf-8")
r3 = subprocess.run([sys.executable, str(SKILL / "scripts" / "assemble_quiz.py"), "n.quiz.json",
                     "--hub", "index.html", "--template", str(SKILL / "assets" / "quiz-template.html")],
                    cwd=nom, capture_output=True, text=True)
check("missing-meta build exit 0", r3.returncode == 0)
check("missing-meta still builds html", (nom / "n.quiz.html").exists())
check("missing-meta skip message", "skipped" in (r3.stdout + r3.stderr))
check("missing-meta no hub written", not (nom / "index.html").exists())

print("\nALL HUB TESTS PASSED")
