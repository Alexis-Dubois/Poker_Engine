from __future__ import annotations
import typing

from Poker_Engine.Deck import Deck
from Poker_Engine.Card import Card

def test_init():
    deck0:Deck = Deck(nbDeck=0)
    deck1:Deck = Deck(nbDeck=1)
    deck2:Deck = Deck(nbDeck=2)

    assert(len(deck0)==0)
    assert(len(deck1)==52)
    assert(len(deck2)==104)

def test_draw_card():
    deck1:Deck = Deck(nbDeck=1)
    deck1.remove_card(Card("A", "♠"))
    assert(len(deck1)==51)
    assert(Card("A", "♠") not in deck1)

def test_choose_random_card():
    deck1:Deck = Deck(nbDeck=1)
    card = deck1.choose_random_card()
    deck1.remove_card(card)
    assert(type(card)==Card)
    assert(len(deck1)==51)
    assert(card not in deck1)

def test_add_card():
    deck1:Deck = Deck(nbDeck=0)
    card = Card("A", "♠")
    deck1.add_card(card)
    assert(len(deck1)==1)
    assert(card in deck1)

def test_remove_card():
    deck1:Deck = Deck(nbDeck=1)
    card = Card("A", "♠")
    deck1.remove_card(card)
    assert(len(deck1)==51)
    assert(card not in deck1)
