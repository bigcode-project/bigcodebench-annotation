from collections import Counter
import random

# Constants
HAND_RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['H', 'D', 'C', 'S']


def f_681():
    """
    Generate a random poker hand consisting of five cards, and count the frequency of each card rank.

    The function creates a list of five cards where each card is a string made up of a rank and a suit (e.g., "10H" for Ten of Hearts).
    It then counts the frequency of each card rank in the hand using a Counter dictionary.

    Parameters:
    - None

    Returns:
    tuple: A tuple containing two elements:
        - hand (list): A list of five cards.
        - rank_count (counter): A Counter dictionary of card ranks with their frequencies in the hand.

    Requirements:
    - collections
    - random

    Example:
        >>> random.seed(42)
        >>> hand, rank_counts = f_681()
        >>> print(hand)  
        ['QH', '2C', '5D', '4H', 'QH']
        >>> print(rank_counts)  
        Counter({'Q': 2, '2': 1, '5': 1, '4': 1})
    """

    hand = []
    for _ in range(5):
        rank = random.choice(HAND_RANKS)
        suit = random.choice(SUITS)
        card = f'{rank}{suit}'
        hand.append(card)

    rank_counts = Counter([card[:-1] for card in hand])

    return hand, rank_counts


import unittest
from collections import Counter

HAND_RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['H', 'D', 'C', 'S']


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(42)

    def test_poker_hand_length(self):
        """Test if the poker hand has 5 cards."""
        hand, rank_counts = f_681()
        self.assertEqual(len(hand), 5, "The poker hand should contain 5 cards.")

    def test_card_format(self):
        """Test if each card in the hand is formatted correctly."""
        hand, rank_counts = f_681()
        for card in hand:
            self.assertIn(len(card), [2, 3],
                          "Each card should be a string of length 2 or 3.")
            self.assertIn(card[:-1], HAND_RANKS,
                          "The rank of each card should be valid.")
            self.assertIn(card[-1], SUITS, "The suit of each card should be valid.")

    def test_rank_counts_type(self):
        """Test if rank_counts is of type Counter."""
        hand, rank_counts = f_681()
        self.assertIsInstance(rank_counts, Counter,
                              "rank_counts should be a Counter dictionary.")

    def test_rank_counts_keys(self):
        """Test if the keys of rank_counts are valid ranks."""
        hand, rank_counts = f_681()
        for rank in rank_counts.keys():
            self.assertIn(rank, HAND_RANKS, "The ranks in rank_counts should be valid.")

    def test_rank_counts_values(self):
        """Test if the values of rank_counts are integers."""
        hand, rank_counts = f_681()
        for count in rank_counts.values():
            self.assertIsInstance(count, int,
                                  "The counts in rank_counts should be integers.")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
