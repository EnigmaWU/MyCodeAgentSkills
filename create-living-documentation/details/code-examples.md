# Code Examples: Living Documentation Extraction & Reconciliation

This file provides code examples in Python and Java for automating glossary extraction, generating system diagrams, and verifying documentation via reconciliation tests.

---

## Section 1: AST Parser and Glossary Extraction

This Python script parses Python files in a target directory, inspects their Abstract Syntax Trees (ASTs), extracts classes decorated with `@Concept` along with their docstrings, and generates a structured Markdown glossary.

```python
import ast
import glob
import os
import sys
from datetime import datetime

def extract_concepts(directory_path):
    concepts = []
    
    # Scan for Python files recursively
    search_path = os.path.join(directory_path, "**", "*.py")
    for file_path in glob.glob(search_path, recursive=True):
        # Ignore test files and setup files
        if "test_" in os.path.basename(file_path) or "setup.py" in file_path:
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                tree = ast.parse(f.read(), filename=file_path)
            except SyntaxError as e:
                print(f"Error parsing {file_path}: {e}", file=sys.stderr)
                sys.exit(1) # Fail fast on syntax errors
                
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    is_concept = False
                    # Check if the class is decorated with 'Concept' or 'concept'
                    for decorator in node.decorator_list:
                        if isinstance(decorator, ast.Name) and decorator.id.lower() == "concept":
                            is_concept = True
                            break
                        elif isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name) and decorator.func.id.lower() == "concept":
                            is_concept = True
                            break
                            
                    if is_concept:
                        docstring = ast.get_docstring(node) or "No description provided."
                        concepts.append({
                            "name": node.name,
                            "file": os.path.relpath(file_path, directory_path),
                            "description": docstring.strip().split("\n")[0] # First line of docstring
                        })
    return concepts

def write_markdown_glossary(concepts, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Living Glossary\n\n")
        f.write(f"*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
        f.write("| Concept | Description | Declared In |\n")
        f.write("| --- | --- | --- |\n")
        for c in sorted(concepts, key=lambda x: x["name"]):
            f.write(f"| `{c['name']}` | {c['description']} | [`{c['file']}`]({c['file']}) |\n")

if __name__ == "__main__":
    src_dir = "./src" # Update to source folder path
    out_file = "./GLOSSARY.md"
    
    print(f"Scanning {src_dir} for concepts...")
    concepts_list = extract_concepts(src_dir)
    print(f"Found {len(concepts_list)} concepts. Writing to {out_file}...")
    write_markdown_glossary(concepts_list, out_file)
    print("Done!")
```

---

## Section 2: Living Diagram Generator Examples

This Python script scans module files, checks import dependencies, and writes a Graphviz DOT script representing the architecture dependencies.

```python
import os
import re

def generate_dependency_graph(source_dir, output_dot_file):
    modules = []
    dependencies = []
    
    # 1. Identify modules
    for filename in os.listdir(source_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            modules.append(filename[:-3]) # Strip .py
            
    # 2. Extract import relationships
    for module in modules:
        filepath = os.path.join(source_dir, f"{module}.py")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            # Simple regex search for local imports
            imports = re.findall(r"^(?:import|from)\s+([a-zA-Z0-9_]+)", content, re.MULTILINE)
            for imp in imports:
                if imp in modules and imp != module:
                    dependencies.append((module, imp))
                    
    # 3. Write Graphviz DOT syntax
    with open(output_dot_file, "w", encoding="utf-8") as f:
        f.write("digraph G {\n")
        f.write("  rankdir=LR;\n")
        f.write("  node [shape=box, style=filled, fillcolor=lightblue, fontname=\"Arial\"];\n")
        f.write("  edge [color=gray, penwidth=1.5];\n\n")
        
        # Nodes
        for mod in modules:
            f.write(f"  \"{mod}\" [label=\"{mod.upper()}\"];\n")
        f.write("\n")
        
        # Edges
        for source, target in sorted(set(dependencies)):
            f.write(f"  \"{source}\" -> \"{target}\";\n")
            
        f.write("}\n")

if __name__ == "__main__":
    generate_dependency_graph("./src/core", "./architecture.dot")
```

---

## Section 3: Reconciliation Test Examples

Reconciliation tests fail the test execution block if the generated glossary drifts from the codebase. The following test searches for documented concepts and validates them.

```python
import unittest
import os
import re

class TestLivingGlossaryReconciliation(unittest.TestCase):
    def setUp(self):
        self.src_dir = os.path.abspath("./src")
        self.glossary_path = os.path.abspath("./GLOSSARY.md")
        
    def test_glossary_contains_all_annotated_classes(self):
        # 1. Gather actual annotated concepts in the source tree
        annotated_concepts = set()
        concept_pattern = re.compile(r"^\s*@concept", re.IGNORECASE)
        class_pattern = re.compile(r"^\s*class\s+([a-zA-Z0-9_]+)")
        
        for root, _, files in os.walk(self.src_dir):
            for file in files:
                if file.endswith(".py") and not file.startswith("test_"):
                    filepath = os.path.join(root, file)
                    with open(filepath, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        
                    for i, line in enumerate(lines):
                        if concept_pattern.match(line):
                            # Search forward to find the class name
                            for j in range(i + 1, min(i + 5, len(lines))):
                                class_match = class_pattern.match(lines[j])
                                if class_match:
                                    annotated_concepts.add(class_match.group(1))
                                    break
                                    
        # 2. Extract documented concepts from GLOSSARY.md
        documented_concepts = set()
        if os.path.exists(self.glossary_path):
            with open(self.glossary_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Find terms written in backticks in the table, e.g., | `UserAccount` |
                documented_concepts = set(re.findall(r"\|\s*`([a-zA-Z0-9_]+)`\s*\|", content))
                
        # 3. Assert zero drift
        missing_in_glossary = annotated_concepts - documented_concepts
        extra_in_glossary = documented_concepts - annotated_concepts
        
        error_msg = []
        if missing_in_glossary:
            error_msg.append(f"Missing in glossary (defined in code but not documented): {missing_in_glossary}")
        if extra_in_glossary:
            error_msg.append(f"Outdated in glossary (documented but does not exist in code): {extra_in_glossary}")
            
        self.assertEqual(len(error_msg), 0, "\n".join(error_msg))

if __name__ == "__main__":
    unittest.main()
```
