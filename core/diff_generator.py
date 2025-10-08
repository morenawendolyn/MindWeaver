"""
Diff generator — produces unified diffs for refactored code suggestions.
"""

import difflib

class DiffGenerator:
    def create_diff(self, original: str, modified: str) -> str:
        diff = difflib.unified_diff(
            original.splitlines(),
            modified.splitlines(),
            fromfile="original",
            tofile="modified",
            lineterm=""
        )
        return "\n".join(diff)
