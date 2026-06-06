# Code Examples: Legacy Mapping & Isolation

This file provides code examples in Python for superimposing metadata, enforcing bubble boundaries, and scanning biodegradable deprecation markers in legacy codebases.

---

## Section 1: Superimposed Metadata Decorators

This Python code demonstrates how to use decorators to add documentation metadata, logging, and translation mappings to legacy classes/methods without modifying their internal execution logic.

```python
import functools
import time

def legacy_metadata(api_id, description, doc_link=None):
    """
    Decorator to superimpose metadata on legacy code.
    Allows tagging functions with system mappings and documentation links.
    """
    def decorator(func):
        # Attach attributes directly to the function object (metadata layer)
        func.api_id = api_id
        func.description = description
        func.doc_link = doc_link
        func.is_legacy = True
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Telemetry/monitoring layer around the legacy code
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"[LEGACY ALERT] Error in legacy endpoint {api_id} ({func.__name__}): {e}")
                raise e
            finally:
                duration = time.time() - start_time
                # Log usage stats for strangler analysis (identifying hot paths)
                print(f"[LEGACY METRIC] {api_id} executed in {duration:.4f}s")
                
        return wrapper
    return decorator

# --- Example Usage on Legacy Code ---

@legacy_metadata(
    api_id="API-402",
    description="Fossilized billing calculation routine. Do not modify directly.",
    doc_link="http://wiki.local/pages/legacy-billing"
)
def calculate_historical_tax(amount, tax_rate):
    # Original, fragile legacy calculation code
    return amount * tax_rate
```

---

## Section 2: Dependency Validation Tests

This Python test scans the codebase import statements to verify boundary constraints—specifically, that new code modules *do not* import from legacy directories directly, enforcing the Bubble Context.

```python
import unittest
import os
import re

class TestBubbleContextBoundaries(unittest.TestCase):
    def setUp(self):
        # Define the paths to analyze
        self.greenfield_dir = os.path.abspath("./src/modern")
        self.legacy_dir_name = "src.legacy" # Import package name of legacy files
        
    def test_greenfield_does_not_import_legacy_directly(self):
        """
        Verify that modern code only communicates with legacy code via the adapter.
        Imports of 'src.legacy' are banned in 'src/modern' except within adapters.
        """
        violations = []
        import_pattern = re.compile(r"^\s*(?:import\s+([a-zA-Z0-9_\.]+)|from\s+([a-zA-Z0-9_\.]+)\s+import)")
        
        for root, _, files in os.walk(self.greenfield_dir):
            for file in files:
                if file.endswith(".py"):
                    # Allow adapter classes to import legacy to perform translations
                    if "adapter" in file or "translation" in file:
                        continue
                        
                    filepath = os.path.join(root, file)
                    with open(filepath, "r", encoding="utf-8") as f:
                        for line_num, line in enumerate(f, 1):
                            match = import_pattern.match(line)
                            if match:
                                imported_module = match.group(1) or match.group(2)
                                if imported_module and imported_module.startswith(self.legacy_dir_name):
                                    relative_path = os.path.relpath(filepath, os.getcwd())
                                    violations.append(
                                        f"{relative_path}:{line_num} -> Banned legacy import: '{imported_module}'"
                                    )
                                    
        # Assert that no boundary violations were detected
        if violations:
            error_message = "\nBoundary Violations (Greenfield files must not import legacy directly):\n" + "\n".join(violations)
            self.fail(error_message)

if __name__ == "__main__":
    unittest.main()
```

---

## Section 3: Biodegradable Annotations Parser

This script scans files for a custom `@biodegradable` decorator and fails the build or prints warnings if the decommissioning deadline has passed.

```python
import ast
import os
import sys
from datetime import datetime

def check_biodegradable_code(directory):
    violations = []
    current_date = datetime.now().date()
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    try:
                        tree = ast.parse(f.read(), filename=filepath)
                    except SyntaxError:
                        continue # Skip syntax errors, handled elsewhere
                        
                    for node in ast.walk(tree):
                        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                            for decorator in node.decorator_list:
                                if isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name) and decorator.func.id == "biodegradable":
                                    # Parse keyword arguments: deadline, owner, replacement
                                    deadline_str = None
                                    owner = "Unknown"
                                    
                                    for kw in decorator.keywords:
                                        if kw.arg == "deadline" and isinstance(kw.value, ast.Constant):
                                            deadline_str = kw.value.value
                                        elif kw.arg == "owner" and isinstance(kw.value, ast.Constant):
                                            owner = kw.value.value
                                            
                                    if deadline_str:
                                        try:
                                            deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d").date()
                                            if current_date > deadline_date:
                                                relative_path = os.path.relpath(filepath, os.getcwd())
                                                violations.append(
                                                    f"{relative_path}::{node.name} - "
                                                    f"Decommission deadline expired on {deadline_str} (Owner: {owner})"
                                                )
                                        except ValueError:
                                            print(f"Invalid date format in {filepath} for {node.name}")
    return violations

# --- Example of Decorator Definition in codebase ---
# def biodegradable(deadline, owner, replacement):
#     def decorator(func):
#         return func
#     return decorator

if __name__ == "__main__":
    src_folder = "./src"
    print("Checking for expired biodegradable code...")
    expired_items = check_biodegradable_code(src_folder)
    
    if expired_items:
        print("\n[ERROR] Expired Legacy Code Blocks Found!", file=sys.stderr)
        for item in expired_items:
            print(f"  - {item}", file=sys.stderr)
        sys.exit(1) # Fail build/test process
    else:
        print("All legacy deadlines are valid.")
```
