from __future__ import annotations
import typing
from collections import defaultdict

from .Card import Card

class Deck:

    def __init__(self, nbDeck:int=1):

        self.stack: set[Card] = set()
        self.color_count: defaultdict[str, int]=defaultdict(lambda:0)
        self.val_count: defaultdict[str, int]=defaultdict(lambda:0)

        for _ in range(nbDeck):
            for color in ["♠", "♥", "♦", "♣"]:
                for val in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
                    self.stack.add(Card(val, color))
                    self.color_count[color] += 1
                    self.val_count[val] += 1
        

            