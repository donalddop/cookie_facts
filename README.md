### Installation

# Create virtual python environment
python -m venv venv
# Activate on linux
source venv/bin/activate
# Activate on Windows powershell
.\venv\Scripts\activate.ps1

# Install requirements
pip install .\requirements.txt

### Building the page
python build.py
# Output is placed in dist folder