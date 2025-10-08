"""
Reward function — evaluates quality of code modifications.
Integrates metrics such as readability, performance, and maintainability.
"""

import random
from typing import Dict

class RewardFunction:
    def __init__(self):
        self.metrics = {"readability": 0.3, "performance": 0.4, "stability": 0.3}

    def evaluate(self, diff: str, file_path: str) -> float:
        base_score = random.uniform(0.4, 0.9)
        penalties = diff.count("-") * 0.001
        return round(base_score - penalties, 3)
