from __future__ import annotations
import typing

# ♠ ♥ ♦ ♣

VAL_TO_NUMERIC: dict[str, int] = {
            "A":100,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "10":10,
            "J":11,
            "Q":12,
            "K":13
        }

class Card:

    def __init__(self, val: str, col: str):
        self.val: str = val
        self.col: str = col
        self.numeric_val: int = VAL_TO_NUMERIC[val]

    def __str__(self) -> str:
        return self.val + self.col

    def __lt__(self, other:Card) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.numeric_val < other.numeric_val
    
    def __eq__(self, other:object) -> bool:
        if type(other) is not Card:
            return False
        return self.numeric_val == other.numeric_val and self.col == other.col
    
    def __hash__(self) -> int:
        return hash((self.val, self.col))