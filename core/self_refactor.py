"""
Self-refactor module — autonomous code improvement loop.
Analyzes the codebase, proposes patches, and validates improvements.
"""

from .code_analyzer import CodeAnalyzer
from .diff_generator import DiffGenerator
from .reward_function import RewardFunction
from .model_adapter import ModelAdapter

class SelfRefactor:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.analyzer = CodeAnalyzer(repo_path)
        self.diff_generator = DiffGenerator()
        self.reward_fn = RewardFunction()
        self.model = ModelAdapter()

    async def improve(self, target_file: str):
        code = self.analyzer.extract_code(target_file)
        suggestions = await self.model.propose_refactor(code)
        diff = self.diff_generator.create_diff(code, suggestions)
        score = self.reward_fn.evaluate(diff, target_file)

        if score > 0.7:
            self.analyzer.apply_diff(target_file, diff)
            return {"file": target_file, "status": "updated", "score": score}
        return {"file": target_file, "status": "skipped", "score": score}
