import unittest
from datetime import datetime, timedelta

from src.models.flashcard import Flashcard


class FlashcardTest(unittest.TestCase):
    def setUp(self):
        self.card = Flashcard('What makes up the United Kingdom?', 'Wales, England, Scotland and Northern Ireland')

    def test_update_freshness(self):
        self.card.created_at = datetime.now().date() - timedelta(days=1)
        self.card.update_freshness()
        self.assertEqual(self.card.freshness, 1)

    def test_update_freshness_same_day(self):
        self.card.created_at = datetime.now().date()
        self.card.update_freshness()
        self.assertEqual(self.card.freshness, 0)

    def test_update_freshness_multiple_days(self):
        self.card.created_at = datetime.now().date() - timedelta(days=3)
        self.card.update_freshness()
        self.card.update_freshness()
        self.card.update_freshness()
        self.assertEqual(self.card.freshness, 3)

    def test_update_freshness_studied_today(self):
        self.card.created_at = datetime.now().date() - timedelta(days=2)
        self.card.last_studied_at = datetime.now().date()
        self.card.freshness = 0
        self.card.update_freshness()
        self.assertEqual(self.card.freshness, 1)

    def test_update_freshness_not_studied_today(self):
        self.card.created_at = datetime.now().date() - timedelta(days=2)
        self.card.last_studied_at = datetime.now().date() - timedelta(days=1)
        self.card.freshness = 0
        self.card.update_freshness()
        self.assertEqual(self.card.freshness, 0)


if __name__ == '__main__':
    unittest.main()
