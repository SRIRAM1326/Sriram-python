import sys
import importlib.util
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

def load_project_module(folder_name: str):
    """Dynamically loads and returns the main.py module from a numbered project directory."""
    module_path = ROOT_DIR / folder_name / "main.py"
    if not module_path.exists():
        raise FileNotFoundError(f"Module file not found: {module_path}")
    
    spec = importlib.util.spec_from_file_location(f"project_{folder_name}", str(module_path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load spec for {folder_name}")
        
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
