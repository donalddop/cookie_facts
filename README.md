# 🍪 Cookie Facts

A static site generator that serves random cookie facts, demonstrating CI/CD automation with GitHub Actions and static hosting workflows.

**Live Demo:** https://donalddop.github.io/cookie_facts/

## What This Demonstrates

- **GitHub Actions CI/CD**: Automated build and deployment pipeline
- **Static Site Generation**: Python-based build script that generates HTML from data
- **GitHub Pages Deployment**: Automated publishing to gh-pages branch
- **Clean Separation**: Data, templates, and build logic kept separate

## Tech Stack

- Python 3.x (build script)
- Jinja2 (templating)
- GitHub Actions (CI/CD)
- GitHub Pages (hosting)

## How It Works

The GitHub Actions workflow automatically:
1. Triggers on every push to `main`
2. Sets up Python environment
3. Installs dependencies
4. Runs `build.py` to generate static HTML
5. Deploys to GitHub Pages

Each build randomly selects a cookie fact from `data/facts.txt` and renders it using the Jinja2 template.

## Local Development
```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
.\venv\Scripts\activate.ps1

# Install dependencies
pip install -r requirements.txt

# Build the site
python build.py

# Output is in dist/index.html
```

## Adding New Facts

Add new cookie facts to `data/facts.txt` (one per line). The next deployment will automatically include them in the random rotation.

## Project Structure
```
cookie_facts/
├── .github/workflows/    # GitHub Actions CI/CD pipeline
├── data/                 # Cookie facts database
├── templates/            # Jinja2 HTML templates
├── tests/                # Test suite
├── build.py             # Static site generator
└── requirements.txt     # Python dependencies
```

## Why This Project?

Built to learn and demonstrate:
- Setting up automated CI/CD pipelines with GitHub Actions
- Static site generation workflows
- Deploying to GitHub Pages programmatically
- Clean project architecture for static sites

---

*Note: The live site shows the same fact on each visit because it's static HTML generated at build time. To see a new fact, trigger a new deployment by pushing to the repo.*