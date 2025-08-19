from __future__ import annotations
import typing

from Poker_Engine.Deck import Deck
from Poker_Engine.Card import Card
from Poker_Engine.Hand import Hand
from Poker_Engine.River import River
from Poker_Engine.PokerHand import PokerHand

def test_has_straight():
    deck: Deck = Deck(nbDeck=1)
    river: River = River(provenance=deck)
    hand1: Hand = Hand(provenance=deck, river=river)
    hand2: Hand = Hand(provenance=deck, river=river)
    hand3: Hand = Hand(provenance=deck, river=river)
    river.add_card(Card('Q', '♠'))
    river.add_card(Card('A', '♥'))
    river.add_card(Card('10', '♠'))
    river.add_card(Card('3', '♥'))
    river.add_card(Card('2', '♠'))
    hand1.add_card(Card('J', '♠'))
    hand1.add_card(Card('K', '♥'))
    hand2.add_card(Card('5', '♠'))
    hand2.add_card(Card('4', '♥'))
    hand3.add_card(Card('K', '♠'))
    hand3.add_card(Card('10', '♣'))
    poker_hand1: PokerHand = PokerHand(hand1, river)
    poker_hand2: PokerHand = PokerHand(hand2, river)
    poker_hand3: PokerHand = PokerHand(hand3, river)
    assert poker_hand1._has_straight()[0] == True
    assert poker_hand2._has_straight()[0] == True
    assert poker_hand3._has_straight()[0] == False

def test_has_flush():
    deck: Deck = Deck(nbDeck=1)
    river: River = River(provenance=deck)
    hand1: Hand = Hand(provenance=deck, river=river)
    hand2: Hand = Hand(provenance=deck, river=river)
    hand3: Hand = Hand(provenance=deck, river=river)
    river.add_card(Card('Q', '♠'))
    river.add_card(Card('A', '♥'))
    river.add_card(Card('10', '♠'))
    river.add_card(Card('3', '♥'))
    river.add_card(Card('2', '♠'))
    hand1.add_card(Card('J', '♠'))
    hand1.add_card(Card('K', '♠'))
    hand2.add_card(Card('5', '♠'))
    hand2.add_card(Card('4', '♠'))
    hand3.add_card(Card('K', '♠'))
    hand3.add_card(Card('10', '♣'))
    poker_hand1: PokerHand = PokerHand(hand1, river)
    poker_hand2: PokerHand = PokerHand(hand2, river)
    poker_hand3: PokerHand = PokerHand(hand3, river)
    assert poker_hand1._has_flush()[0] == True
    assert poker_hand2._has_flush()[0] == True
    assert poker_hand3._has_flush()[0] == False

def test_find_best_poker_hand():
    deck: Deck = Deck(nbDeck=1)
    river: River = River(provenance=deck)
    hand1: Hand = Hand(provenance=deck, river=river)
    hand2: Hand = Hand(provenance=deck, river=river)
    hand3: Hand = Hand(provenance=deck, river=river)
    river.add_card(Card('Q', '♠'))
    river.add_card(Card('A', '♠'))
    river.add_card(Card('10', '♠'))
    river.add_card(Card('3', '♠'))
    river.add_card(Card('2', '♣'))
    hand1.add_card(Card('J', '♠'))
    hand1.add_card(Card('K', '♠'))
    hand2.add_card(Card('5', '♠'))
    hand2.add_card(Card('7', '♠'))
    hand3.add_card(Card('K', '♥'))
    hand3.add_card(Card('10', '♣'))
    poker_hand1: PokerHand = PokerHand(hand1, river)
    poker_hand2: PokerHand = PokerHand(hand2, river)
    poker_hand3: PokerHand = PokerHand(hand3, river)
    assert poker_hand1._find_best_poker_hand().type == "straight_flush"
    assert poker_hand1._find_best_poker_hand().best_group_value == "A"
    assert poker_hand2._find_best_poker_hand().type == "flush"
    assert poker_hand2._find_best_poker_hand().best_group_value == None
    assert poker_hand3._find_best_poker_hand().type == "pair"
    assert poker_hand3._find_best_poker_hand().best_group_value == "10"

    deck: Deck = Deck(nbDeck=1)
    river: River = River(provenance=deck)
    hand1: Hand = Hand(provenance=deck, river=river)
    hand2: Hand = Hand(provenance=deck, river=river)
    hand3: Hand = Hand(provenance=deck, river=river)
    river.add_card(Card('Q', '♠'))
    river.add_card(Card('Q', '♣'))
    river.add_card(Card('Q', '♥'))
    river.add_card(Card('3', '♠'))
    river.add_card(Card('2', '♣'))
    hand1.add_card(Card('Q', '♦'))
    hand1.add_card(Card('K', '♠'))
    hand2.add_card(Card('5', '♠'))
    hand2.add_card(Card('7', '♠'))
    hand3.add_card(Card('K', '♥'))
    hand3.add_card(Card('K', '♣'))
    poker_hand1: PokerHand = PokerHand(hand1, river)
    poker_hand2: PokerHand = PokerHand(hand2, river)
    poker_hand3: PokerHand = PokerHand(hand3, river)
    assert poker_hand1._find_best_poker_hand().type == "four_of_a_kind"
    assert poker_hand1._find_best_poker_hand().best_group_value == "Q"
    assert poker_hand2._find_best_poker_hand().type == "three_of_a_kind"
    assert poker_hand2._find_best_poker_hand().best_group_value == "Q"
    assert poker_hand3._find_best_poker_hand().type == "full_house"
    assert poker_hand3._find_best_poker_hand().best_group_value == "Q"
    assert poker_hand3._find_best_poker_hand().second_best_group_value == "K"

    deck: Deck = Deck(nbDeck=1)
    river: River = River(provenance=deck)
    hand1: Hand = Hand(provenance=deck, river=river)
    hand2: Hand = Hand(provenance=deck, river=river)
    river.add_card(Card('A', '♠'))
    river.add_card(Card('2', '♣'))
    river.add_card(Card('3', '♥'))
    river.add_card(Card('4', '♠'))
    river.add_card(Card('9', '♣'))
    hand1.add_card(Card('A', '♦'))
    hand1.add_card(Card('2', '♠'))
    hand2.add_card(Card('7', '♠'))
    hand2.add_card(Card('8', '♠'))
    poker_hand1: PokerHand = PokerHand(hand1, river)
    poker_hand2: PokerHand = PokerHand(hand2, river)
    poker_hand3: PokerHand = PokerHand(hand3, river)
    assert poker_hand1._find_best_poker_hand().type == "two_pairs"
    assert poker_hand1._find_best_poker_hand().best_group_value == "A"
    assert poker_hand1._find_best_poker_hand().second_best_group_value == "2"
    assert poker_hand2._find_best_poker_hand().type == "high_card"
    assert poker_hand2._find_best_poker_hand().best_group_value == "A"

def test_less_than():
    deck: Deck = Deck(nbDeck=1)
    river: River = River(provenance=deck)
    hand1: Hand = Hand(provenance=deck, river=river)
    hand2: Hand = Hand(provenance=deck, river=river)
    hand3: Hand = Hand(provenance=deck, river=river)
    river.add_card(Card('Q', '♠'))
    river.add_card(Card('Q', '♣'))
    river.add_card(Card('Q', '♥'))
    river.add_card(Card('3', '♠'))
    river.add_card(Card('2', '♣'))
    hand1.add_card(Card('Q', '♦'))
    hand1.add_card(Card('K', '♠'))
    hand2.add_card(Card('5', '♠'))
    hand2.add_card(Card('7', '♠'))
    hand3.add_card(Card('K', '♥'))
    hand3.add_card(Card('K', '♣'))
    poker_hand1: PokerHand = PokerHand(hand1, river)
    poker_hand2: PokerHand = PokerHand(hand2, river)
    poker_hand3: PokerHand = PokerHand(hand3, river)
    assert poker_hand2 < poker_hand1
    assert poker_hand3 < poker_hand1
    assert poker_hand2 < poker_hand3

def test_equal():
    deck: Deck = Deck(nbDeck=1)
    river: River = River(provenance=deck)
    hand1: Hand = Hand(provenance=deck, river=river)
    hand2: Hand = Hand(provenance=deck, river=river)
    hand3: Hand = Hand(provenance=deck, river=river)
    river.add_card(Card('A', '♠'))
    river.add_card(Card('2', '♣'))
    river.add_card(Card('3', '♥'))
    river.add_card(Card('4', '♠'))
    river.add_card(Card('9', '♣'))
    hand1.add_card(Card('10', '♦'))
    hand1.add_card(Card('Q', '♠'))
    hand2.add_card(Card('10', '♠'))
    hand2.add_card(Card('Q', '♠'))
    hand3.add_card(Card('7', '♣'))
    hand3.add_card(Card('K', '♠'))
    poker_hand1: PokerHand = PokerHand(hand1, river)
    poker_hand2: PokerHand = PokerHand(hand2, river)
    poker_hand3: PokerHand = PokerHand(hand3, river)
    assert poker_hand1 == poker_hand2
    assert poker_hand1 != poker_hand3
