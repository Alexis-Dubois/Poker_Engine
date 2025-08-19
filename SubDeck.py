from __future__ import annotations
import typing
from collections import defaultdict

from Poker_Engine.Card import Card
from Poker_Engine.Deck import Deck

class SubDeck(Deck):
    
    def __init__(self, provenance: Deck):
        super().__init__(nbDeck=0)
        self.cards: defaultdict[Card, int] = defaultdict(lambda: 0)
        self.provenance: Deck = provenance
        self.max_size: int = 0 # must be overwritten by subclasses

    def add_card(self, card: Card) -> None:
        super().add_card(card)
        self.provenance.remove_card(card)

    def create_virtual_filled_copy(self) -> SubDeck:
        virtual_copy = SubDeck(self.provenance)
        virtual_copy.max_size = self.max_size
        virtual_copy.cards = self.cards.copy()
        virtual_copy.color_count = self.color_count.copy()
        virtual_copy.val_count = self.val_count.copy()
        while len(virtual_copy) < virtual_copy.max_size:
            new_card = self.provenance.choose_random_card()
            virtual_copy.add_card(new_card)
        return virtual_copy