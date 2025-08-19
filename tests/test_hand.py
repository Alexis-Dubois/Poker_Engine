from Poker_Engine.Hand import Hand
from Poker_Engine.Card import Card
from Poker_Engine.Deck import Deck
from Poker_Engine.River import River

def test_hand_add_card():
    deck = Deck(nbDeck=1)
    river = River(provenance=deck)
    hand = Hand(provenance=deck, river=river)
    hand.add_card(Card('A', '♠'))
    hand.add_card(Card('Q', '♥'))
    assert len(hand.cards) == 2
    assert Card('A', '♠') in hand.cards
    assert Card('Q', '♥') in hand.cards
    assert hand.color_count['♠'] == 1
    assert hand.val_count['A'] == 1
    assert len(deck) == 50
    assert Card('A', '♠') not in deck
    assert Card('Q', '♥') not in deck
    assert deck.color_count['♠'] == 12
    assert deck.val_count['A'] == 3
    assert len(river) == 0

def test_create_virtual_filled_copy():
    deck = Deck(nbDeck=1)
    river = River(provenance=deck)
    hand = Hand(provenance=deck, river=river)
    hand.add_card(Card('A', '♠'))
    virtual_copy = hand.create_virtual_filled_copy()
    assert len(virtual_copy) == hand.max_size
    assert virtual_copy.color_count['♠'] >= 1
    assert len(deck) == 50
    assert Card('A', '♠') not in deck
    assert deck.color_count['♠'] <= 12
    assert deck.val_count['A'] <= 3

def test_calculate_winning_chance():
    deck = Deck(nbDeck=1)
    river = River(provenance=deck)
    hand1 = Hand(provenance=deck, river=river)
    hand2 = Hand(provenance=deck, river=river)
    hand3 = Hand(provenance=deck, river=river)
    river.add_card(Card('Q', '♠'))
    river.add_card(Card('A', '♠'))
    river.add_card(Card('10', '♠'))
    river.add_card(Card('5', '♥'))
    river.add_card(Card('6', '♠'))
    hand1.add_card(Card('J', '♠'))
    hand1.add_card(Card('K', '♠'))
    hand2.add_card(Card('2', '♥'))
    hand2.add_card(Card('3', '♥'))
    hand3.add_card(Card('10', '♣'))
    hand3.add_card(Card('A', '♣'))
    
    assert 1 >= hand1.calculate_winning_chance(nb_players_left=3) > 0.99
    assert 0 <= hand2.calculate_winning_chance(nb_players_left=3) < 0.01
    assert 0 <= hand3.calculate_winning_chance(nb_players_left=3) <= 1.0
