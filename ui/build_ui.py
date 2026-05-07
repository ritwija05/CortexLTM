import pathlib, os

OUT = pathlib.Path(__file__).parent

# ── helpers ──────────────────────────────────────────────────────────────────
def w(name, content):
    (OUT / name).write_text(content, encoding="utf-8")
    print(f"  wrote {name} ({len(content):,} bytes)")

# ── HTML ─────────────────────────────────────────────────────────────────────
HTML = ""
exec(open(OUT / "html_parts.py").read())

# ── CSS ──────────────────────────────────────────────────────────────────────
CSS = ""
exec(open(OUT / "css_parts.py").read())

# ── JS ───────────────────────────────────────────────────────────────────────
JS = ""
exec(open(OUT / "js_parts.py").read())

w("index.html", HTML)
w("style.css",  CSS)
w("app.js",     JS)
print("Done ✓")
