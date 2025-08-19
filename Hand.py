from __future__ import annotations
import typing
from collections import defaultdict
from time import time

from Poker_Engine.Card import Card
from Poker_Engine.Deck import Deck
from Poker_Engine.SubDeck import SubDeck
from Poker_Engine.River import River
from Poker_Engine.PokerHand import PokerHand

class Hand(SubDeck):
    
    def __init__(self, provenance: Deck, river: River):
        super().__init__(provenance)
        self.river: River = river
        self.max_size: int = 2  # The hand can have a maximum of 2 cards

    def calculate_winning_chance(self, nb_players_left:int = 2, allowed_time: float=1.0) -> float:
        nb_simulated_outcomes: int = 0
        nb_simulated_wins: int = 0
        win_ratio: float = 0.0
        starting_time: float = time()
        while time() - starting_time < allowed_time:
            simulated_poker_hands: list[PokerHand] = [] # index 0 is current hand, 
            simulated_poker_hands.append(PokerHand(self.create_virtual_filled_copy(), self.river.create_virtual_filled_copy()))
            for opponent in range(nb_players_left - 1):
                simulated_poker_hands.append(PokerHand(Hand(self.provenance,self.river).create_virtual_filled_copy(), self.river.create_virtual_filled_copy()))
            if max(simulated_poker_hands) == simulated_poker_hands[0]:
                nb_simulated_wins += 1
            nb_simulated_outcomes += 1

        if nb_simulated_outcomes > 0:
            win_ratio = nb_simulated_wins / nb_simulated_outcomes

        return win_ratio