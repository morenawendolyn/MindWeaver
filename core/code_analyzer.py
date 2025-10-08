"""
Static and semantic code analysis module.
Provides AST-based insights and quality metrics for agent decision making.
"""

import ast
from typing import Dict, Any

class CodeAnalyzer:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path

    def extract_code(self, file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def analyze_ast(self, code: str) -> Dict[str, Any]:
        tree = ast.parse(code)
        functions = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
        complexity = len(functions) * 0.1
        return {"functions": functions, "complexity": complexity}

    def apply_diff(self, file_path: str, diff: str):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(diff)
