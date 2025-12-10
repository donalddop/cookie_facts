import sys
from pathlib import Path
import importlib.util

# Load build.py as module
spec = importlib.util.spec_from_file_location("build", "build.py")
build = importlib.util.module_from_spec(spec)
sys.modules["build"] = build
spec.loader.exec_module(build)

def test_build_generates_file():
    # Just check that dist/index.html was created
    dist_dir = Path("dist")
    output_file = dist_dir / "index.html"
    
    assert output_file.exists(), "dist/index.html should exist after build"
    
    # Check it has content
    content = output_file.read_text()
    assert len(content) > 0, "Output file should not be empty"
    assert "Cookie Facts" in content, "Should contain title"
    assert "<script>" in content, "Should contain JavaScript"

def test_facts_file_exists():
    facts_file = Path("data/facts.txt")
    assert facts_file.exists(), "facts.txt should exist"
    
    facts = [line.strip() for line in facts_file.read_text().splitlines() if line.strip()]
    assert len(facts) > 0, "Should have at least one fact"