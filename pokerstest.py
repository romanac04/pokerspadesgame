import unittest
from main import check_straight,check_3ofa_kind, check_royal_flush, play_cards
class MyTestCase(unittest.TestCase):
    def test_check_straight(self):
        self.assertEqual(check_straight('S5', 'S6', 'S7'), 7)
        self.assertEqual(check_straight('S6', 'S5', 'S7'), 7)# add assertion here
        self.assertEqual(check_straight('S3', 'SQ', 'SK'), 0)
        self.assertEqual(check_straight('SA', 'S2', 'S3'), 0)

    def test_three_of_a_kind(self):
        self.assertEqual(check_3ofa_kind('S9', 'S9', 'S9'), 9)
        self.assertEqual(check_3ofa_kind('SA', 'SA', 'SA'), 14)
        self.assertEqual(check_3ofa_kind('S2', 'S2', 'S2'), 2)
        self.assertEqual(check_3ofa_kind('SJ', 'SQ', 'SJ'), 0)

    def test_check_royal_flush(self):
        self.assertEqual(check_royal_flush('SA', 'SK', 'SQ'), 14)
        self.assertEqual(check_royal_flush('S10', 'SJ', 'SQ'), 0)
        self.assertEqual(check_royal_flush('SJ', 'SQ', 'SK'), 0)

    def test_play_cards(self):
        self.assertEqual(play_cards('S2', 'S3', 'S4', 'S5', 'S6', 'S7'), 1)
        self.assertEqual(play_cards('S2', 'S3', 'S4', 'S4', 'S4', 'S5'), -1)
        self.assertEqual(play_cards('S2', 'S2', 'S2', 'SA', 'SK', 'SQ'), 1)
        self.assertEqual(play_cards('S10', 'SJ', 'SQ', 'SK', 'SA', 'S2'),-1)
        self.assertEqual(play_cards('S7', 'S7', 'S5', 'SK', 'S5', 'S5'), 0)

if __name__ == '__main__':
    unittest.main()
