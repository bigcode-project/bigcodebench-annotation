import random
from collections import Counter

# Constants
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def f_267(x=1):
    """
    Draw x random 5-card poker hands from a 52-card pack (without suits) and return
    the hands along with a counter of the drawn cards.

    Parameters:
    x (int, optional): Number of hands to draw. Default is 1.

    Returns:
    tuple: A tuple containing two elements:
        - list of list str: Each inner list contains 5 strings, representing a 5-card poker hand.
        - Counter: A counter of the drawn cards.


    The output is random; hence, the returned list will vary with each call.

    Requirements:
    - random
    - collections.Counter

    Example:
    >>> result = f_267(1)
    >>> len(result[0][0])
    5
    >>> result[0][0] in CARDS:
    True
    """
    result = []
    card_counts = Counter()

    for i in range(x):
        drawn = random.sample(CARDS, 5)
        result.append(drawn)
        card_counts.update(drawn)

    return result, card_counts

import unittest

class TestDrawPokerHand(unittest.TestCase):

    def test_hand_size(self):
        """ Test if the hand contains exactly 5 cards. """
        hand, _ = f_267()
        self.assertEqual(len(hand[0]), 5)
    
    
    def test_drawn_size(self):
        hand, _ = f_267(2)
        self.assertEqual(len(hand[0]), 5)
        self.assertEqual(len(hand), 2)

    
    def test_counter(self):
        hand, counter = f_267(1)
        self.assertEqual(len(hand[0]), 5)
        self.assertLessEqual(counter[hand[0][0]], 5)
        self.assertGreaterEqual(counter[hand[0][0]], 1)


    def test_card_uniqueness(self):
        """ Test if all cards in the hand are unique. """
        hand, _ = f_267()
        self.assertEqual(len(hand[0]), len(set(hand[0])))

    def test_valid_cards(self):
        """ Test if all cards drawn are valid card values. """
        hand, _ = f_267()
        for card in hand[0]:
            self.assertIn(card, ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])

    def test_randomness(self):
        """ Test if multiple executions return different hands. """
        hands = [f_267()[0][0] for _ in range(10)]
        self.assertTrue(len(set(tuple(hand) for hand in hands[0])) > 1)

    def test_card_distribution(self):
        """ Test if all possible cards appear over multiple executions. """
        all_cards = set()
        for _ in range(1000):
            all_cards.update(f_267()[0][0])
        self.assertEqual(all_cards, set(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']))

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDrawPokerHand))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    run_tests()
