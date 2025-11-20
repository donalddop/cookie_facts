from build import generate_page
from pathlib import Path

def test_build_generates_file():
    generate_page()
    assert Path("dist/index.html").exists()
