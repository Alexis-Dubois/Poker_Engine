from __future__ import annotations
import typing
from collections import defaultdict, namedtuple

from Poker_Engine.Card import Card, VAL_TO_NUMERIC
from Poker_Engine.Deck import Deck
from Poker_Engine.SubDeck import SubDeck

STRAIGHT_ORDER = ["A","K","Q","J","10","9","8","7","6","5","4","3","2","A"]
RANKED_HANDS = ["straight_flush", "four_of_a_kind", "full_house", "flush", "straight", "three_of_a_kind", "two_pairs", "pair", "high_card"]
class HandInfo(typing.NamedTuple):
    type: str  # type of poker hand
    best_group_value: str | None # not used for a flush that is not straight
    second_best_group_value: str | None

class PokerHand(Deck):
    
    def __init__(self, hand: SubDeck, river: SubDeck):
        super().__init__(0)
        for card, count in river.cards.items():
            for _ in range(count):
                self.add_card(card)
        for card, count in hand.cards.items():
            for _ in range(count):
                self.add_card(card)

        self.poker_hand: HandInfo = self._find_best_poker_hand()

    def _find_best_poker_hand(self) -> HandInfo:
        """
        finds the best poker hand we can make with our river and hand
        """
        has_straight, straight_high = self._has_straight()
        has_flush, flush_color = self._has_flush()

        # straight_flush check
        if has_straight and has_flush:
            has_straight_flush, straight_high = self._has_straight_flush(flush_color, straight_high)
            if has_straight_flush:
                return HandInfo("straight_flush", str(straight_high), None)

        # general value analysis
        highest_four_group: str | None = None
        highest_three_group: str | None = None
        highest_two_group: str | None = None
        second_highest_two_group: str | None = None
        highest_single: str | None = None

        for val in ["A","K","Q","J","10","9","8","7","6","5","4","3","2","A"]:
            if self.val_count[val] >= 1 and highest_single is None:
                highest_single = val
            if self.val_count[val] >= 4 and highest_four_group is None:
                highest_four_group = val
            elif self.val_count[val] == 3 and highest_three_group is None:
                highest_three_group = val
            elif self.val_count[val] == 2:
                if highest_two_group is None:
                    highest_two_group = val
                elif second_highest_two_group is None:
                    second_highest_two_group = val

        if highest_four_group is not None:
            return HandInfo("four_of_a_kind", highest_four_group, None)
        elif highest_three_group is not None and highest_two_group is not None:
            return HandInfo("full_house", highest_three_group, highest_two_group)
        elif has_flush:
            return HandInfo("flush", None, None)
        elif has_straight:
            return HandInfo("straight", str(straight_high), None)
        elif highest_three_group is not None:
            return HandInfo("three_of_a_kind", highest_three_group, None)
        elif second_highest_two_group is not None:
            return HandInfo("two_pairs", highest_two_group, second_highest_two_group)
        elif highest_two_group is not None:
            return HandInfo("pair", highest_two_group, second_highest_two_group)
        else:
            return HandInfo("high_card", highest_single, None)

    def _has_straight(self) -> tuple[bool, str | None]:
        """
        detect if there is a straight in the hand
        bool: whether a straight is present
        str: highest card value in the straight
        """
        current_straight_length: int = 0
        highest: str | None = None

        for val in ["A","K","Q","J","10","9","8","7","6","5","4","3","2","A"]:
            if self.val_count[val] < 1: # no card to continue straight
                current_straight_length = 0
                continue
            if current_straight_length == 0: # new straight
                highest = val
            current_straight_length+=1
            if current_straight_length >= 5: # straight found
                return (True, highest)
        return (False, None)

    def _has_flush(self) -> tuple[bool, str | None]:
        """
        detect if there is a flush in the hand
        bool: whether a flush is present
        str: highest card color in the flush
        """
        for color, count in self.color_count.items():
            if count >= 5:
                return (True, color)
        return (False, None)

    def _has_straight_flush(self, color, high) -> tuple[bool, str | None]:
        """
        detect if there is a straight flush in the hand
        bool: whether a straight flush is present
        str: highest card value in the straight flush
        """
        values: list[str] = STRAIGHT_ORDER
        position: int = values.index(high)
        for val in values[position:position+5]:
            if Card(val, color) in self.cards:
                continue
            else:
                return (False, None)
        return (True, high)
    
    def __lt__(self, other:object) -> bool:
        if not isinstance(other, PokerHand):
            return NotImplemented
        o: PokerHand = typing.cast(PokerHand, other)
        if self.poker_hand.type == o.poker_hand.type:
            if self.poker_hand.best_group_value == o.poker_hand.best_group_value:
                if self.poker_hand.second_best_group_value == o.poker_hand.second_best_group_value:
                    return self._tie_breaker(o)
                else: # different second best group values
                    return VAL_TO_NUMERIC[str(self.poker_hand.second_best_group_value)] < VAL_TO_NUMERIC[str(o.poker_hand.second_best_group_value)]
            else: # different best group values
                return VAL_TO_NUMERIC[str(self.poker_hand.best_group_value)] < VAL_TO_NUMERIC[str(o.poker_hand.best_group_value)]
        return RANKED_HANDS.index(self.poker_hand.type) > RANKED_HANDS.index(o.poker_hand.type)    
    
    def _tie_breaker(self, other:PokerHand):
        """
        returns True if self loses the tie (self < other)
        """
        self_card_list:list[Card] = sorted(self.cards, reverse=True)
        other_card_list:list[Card] = sorted(other.cards, reverse=True)
        for self_card, other_card in zip(self_card_list, other_card_list):
            if self_card < other_card:
                return True
            elif other_card < self_card:
                return False
        return False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PokerHand):
            return NotImplemented
        o: PokerHand = typing.cast(PokerHand, other)
        return not self < o and not o < self
