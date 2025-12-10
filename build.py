hell yeah lets make it interesting

10:14 PM
Updated build.py with JS rotation
Code 
Updated index.html template
Interactive artifact 
Nice! Here's what I upgraded:

Changes:

Client-side rotation - All facts are embedded in the HTML as JSON, JavaScript picks a random one on each button click
Better design - Floating cookie animation, gradient background, smooth transitions
Progress tracker - Shows how many facts you've seen out of the total
Smooth animations - Fade effect when switching facts
How to update your repo:

Replace templates/index.html with the new template
Replace build.py with the updated script
Commit and push:
bash
git add build.py templates/index.html
git commit -m "Add client-side fact rotation with animations"
git push
GitHub Actions will rebuild and deploy automatically. Now every time someone clicks "Get Another Fact!" they'll see a new random fact, and it tracks how many unique facts they've discovered.

The page also looks way better now with the floating cookie and gradient background. Want to see it? Push the changes and wait ~2 minutes for GitHub Actions to deploy.



Want to be notified when Claude responds?





Claude is AI and can make mistakes. Please double-check responses.
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
