from dataclasses import dataclass
from typing import Optional

@dataclass
class Expense:
    description: str
    amount: float
    createdAt: str
    updatedAt: str
    id: Optional[str] = None