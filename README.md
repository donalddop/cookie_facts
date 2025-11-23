# Cookie Facts

This project is a simple static site generator that displays a random cookie fact each time you build the site.

### Installation

# Create virtual python environment
python -m venv venv
# Activate on linux
source venv/bin/activate
# Activate on Windows powershell
.\venv\Scripts\activate.ps1

# Install requirements
pip install -r requirements.txt

### Building the page
python build.py
# Output is placed in dist folder

### Usage

Open the `dist/index.html` file in your web browser to see the cookie fact.

### Contributing

To add a new cookie fact, simply add a new line to the `data/facts.txt` file.