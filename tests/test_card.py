from __future__ import annotations
import typing

from Poker_Engine.Deck import Deck
from Poker_Engine.Card import Card

def test_card_equality():
    card1 = Card("A", "♠")
    card2 = Card("A", "♠")
    card3 = Card("K", "♦")
    assert(card1 == card2)
    assert(card1 != card3)
