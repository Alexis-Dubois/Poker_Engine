from __future__ import annotations
import typing

from ..Deck import Deck

def test_init():
    deck0:Deck = Deck(nbDeck=0)
    deck1:Deck = Deck(nbDeck=1)
    deck2:Deck = Deck(nbDeck=2)

    assert(len(deck0.stack)==0)
    assert(len(deck1.stack)==52)
    assert(len(deck2.stack)==104)
