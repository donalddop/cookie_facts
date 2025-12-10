import json
import random
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Setup paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
TEMPLATES_DIR = BASE_DIR / "templates"
DIST_DIR = BASE_DIR / "dist"

# Create dist directory
DIST_DIR.mkdir(exist_ok=True)

# Load all facts
facts_file = DATA_DIR / "facts.txt"
with open(facts_file, 'r', encoding='utf-8') as f:
    facts = [line.strip() for line in f if line.strip()]

# Setup Jinja2
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = env.get_template('index.html')

# Render with all facts as JSON for client-side rotation
html = template.render(facts_json=json.dumps(facts))

# Write output
output_file = DIST_DIR / "index.html"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Built site with {len(facts)} cookie facts")
print(f"✓ Output: {output_file}")