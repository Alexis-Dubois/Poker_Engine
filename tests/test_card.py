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

def test_less_than():
    card1 = Card("2", "♠")
    card2 = Card("K", "♦")
    card3 = Card("K", "♠")
    assert(card1 < card2)
    assert(not (card2 < card2))
    assert(not (card2 < card3))

def test_to_string():
    card1 = Card("A", "♠")
    card2 = Card("K", "♦")
    assert(str(card1) == "A♠")
    assert(str(card2) == "K♦")