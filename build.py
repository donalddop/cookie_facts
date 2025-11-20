from pathlib import Path
import random

def generate_page():
    facts_path = Path("data/facts.txt")
    template_path = Path("templates/index.html")
    dist_path = Path("dist")
    dist_path.mkdir(exist_ok=True)

    facts = facts_path.read_text(encoding="utf-8").splitlines()
    chosen = random.choice(facts)

    template = template_path.read_text(encoding="utf-8")
    html = template.replace("{{FACT}}", chosen)

    (dist_path / "index.html").write_text(html, encoding="utf-8")

if __name__ == "__main__":
    generate_page()
