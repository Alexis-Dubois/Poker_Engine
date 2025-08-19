from Poker_Engine.Hand import Hand
from Poker_Engine.Card import Card
from Poker_Engine.Deck import Deck
from Poker_Engine.River import River

def test_hand_add_card():
    deck = Deck(nbDeck=1)
    river = River(provenance=deck)
    river.add_card(Card('A', '♠'))
    river.add_card(Card('Q', '♥'))
    assert len(river.cards) == 2
    assert Card('A', '♠') in river.cards
    assert Card('Q', '♥') in river.cards
    assert river.color_count['♠'] == 1
    assert river.val_count['A'] == 1
    assert len(deck) == 50
    assert Card('A', '♠') not in deck
    assert Card('Q', '♥') not in deck
    assert deck.color_count['♠'] == 12
    assert deck.val_count['A'] == 3

def test_create_virtual_filled_copy():
    deck = Deck(nbDeck=1)
    river = River(provenance=deck)
    river.add_card(Card('A', '♠'))
    virtual_copy = river.create_virtual_filled_copy()
    assert len(virtual_copy) == river.max_size
    assert virtual_copy.color_count['♠'] >= 1
    assert len(deck) == 47
    assert Card('A', '♠') not in deck
    assert deck.color_count['♠'] <= 12
    assert deck.val_count['A'] <= 3