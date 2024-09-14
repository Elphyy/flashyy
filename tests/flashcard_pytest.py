import pytest
from datetime import datetime, timedelta
from src.models.flashcard import Flashcard

@pytest.fixture
def flashcard():
    return Flashcard('What makes up the United Kingdom?', 'Wales, England, Scotland and Northern Ireland')

def test_update_freshness(flashcard):
    flashcard.created_at = datetime.now().date() - timedelta(days=1)
    flashcard.update_freshness()
    assert flashcard.freshness == 1

def test_update_freshness_same_day(flashcard):
    flashcard.created_at = datetime.now().date()
    flashcard.update_freshness()
    assert flashcard.freshness == 0

def test_update_freshness_multiple_days(flashcard):
    flashcard.created_at = datetime.now().date() - timedelta(days=3)
    flashcard.update_freshness()
    flashcard.update_freshness()
    flashcard.update_freshness()
    assert flashcard.freshness == 3

def test_update_freshness_studied_today(flashcard):
    flashcard.created_at = datetime.now().date() - timedelta(days=2)
    flashcard.last_studied_at = datetime.now().date()
    flashcard.freshness = 0
    flashcard.update_freshness()
    assert flashcard.freshness == 1

def test_update_freshness_not_studied_today(flashcard):
    flashcard.created_at = datetime.now().date() - timedelta(days=2)
    flashcard.last_studied_at = datetime.now().date() - timedelta(days=1)
    flashcard.freshness = 0
    flashcard.update_freshness()
    assert flashcard.freshness == 0
