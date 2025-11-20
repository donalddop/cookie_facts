from pathlib import Path
import importlib.util

# Dynamically load build.py
build_path = Path(__file__).parent.parent / "build.py"
spec = importlib.util.spec_from_file_location("build", build_path)
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

def test_build_generates_file():
    build.generate_page()
    assert Path("dist/index.html").exists()
