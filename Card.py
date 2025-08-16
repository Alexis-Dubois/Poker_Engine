from __future__ import annotations
import typing

# ♠ ♥ ♦ ♣

VAL_TO_NUMERIC: dict = {
            "A":1,
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