from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Event:
    t: int
    action: str
    spaces: Dict[str, Any]

    def __lt__(self, other):
        return self.t < other.t

    def __le__(self, other):
        return self.t <= other.t

    def __gt__(self, other):
        return self.t > other.t

    def __ge__(self, other):
        return self.t >= other.t
