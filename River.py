from __future__ import annotations
import typing

from Poker_Engine.SubDeck import SubDeck
from Poker_Engine.Deck import Deck

class River(SubDeck):
    
    def __init__(self, provenance: Deck):
        super().__init__(provenance)
        self.max_size: int = 5  # The river can have a maximum of 5 cards
