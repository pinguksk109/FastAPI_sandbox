from typing import Dict

class UsageInfo:
    def __init__(self, limit: int, row: Dict):
        self.limit = limit
        self.row = row

    def get_count(self) -> int:
        return len(self.row)