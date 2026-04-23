from pathlib import Path

CONTENT_DIR = Path(__file__).resolve().parents[1] / "content"

def load_markdown(name: str, fallback: str = "") -> str:
    path = CONTENT_DIR / name
    if path.exists():
        return path.read_text(encoding="utf-8")
    return fallback
