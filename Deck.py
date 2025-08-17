from __future__ import annotations
import typing
from collections import defaultdict
from random import choice

from Poker_Engine.Card import Card

class Deck:

    def __init__(self, nbDeck:int=1):

        self.unknown: defaultdict[Card, int] = defaultdict(lambda: 0)
        self.color_count: defaultdict[str, int]=defaultdict(lambda:0)
        self.val_count: defaultdict[str, int]=defaultdict(lambda:0)

        for _ in range(nbDeck):
            for color in ["♠", "♥", "♦", "♣"]:
                for val in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
                    self.unknown[Card(val, color)] += 1
                    self.color_count[color] += 1
                    self.val_count[val] += 1
    
    def remove_card(self, card:Card) -> None:
        """
        Remove a specific card from the deck.
        """
        self.unknown[card] -= 1
        self.color_count[card.col] -= 1
        self.val_count[card.val] -= 1

    def __contains__(self, card: Card) -> bool:
        return self.unknown[card] > 0

    def __len__(self) -> int:
        return sum(self.unknown.values())
    
    def draw_random_card(self) -> Card:
        picked = choice(tuple(self.unknown))
        self.unknown[picked] -= 1
        return picked
        
    