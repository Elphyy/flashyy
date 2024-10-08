# This file implement the logic behind the flashcard system.
# A flashcard is a card bearing a question and an answer.
import json
from datetime import datetime, timedelta
from uuid import uuid4


class Flashcard:
    """The Flashcard class is used to hold flashcard object data."""
    ID: uuid4()
    question: str
    answer: str
    elo: int
    freshness: int
    created_at: datetime.now().date()
    last_studied_at: datetime.now().date()

    def __init__(self, question :str, answer :str):
        """
        Initialize a Flashcard object.
        The Elo rating, initially set to 50, represents the question's difficulty; it adjusts based on the user's performance when answering the question (cf. update_elo() function).
        The freshness value, initially set to 0, indicates how recently the card was answered; it influences the question's Elo rating and is updated daily when the user responds to the card (cf. update_freshness() function)
        :param question: string representing the question asked.
        :param answer: string representing the answer wanted.
        """
        self.ID = uuid4()
        self.question = question
        self.answer = answer
        self.elo = 50
        self.freshness = 0
        self.created_at = datetime.now().date()
        self.last_studied_at = datetime.now().date()

    def update_elo(self) -> int:
        return 0

    def update_freshness(self) -> None:
        current_date = datetime.now().date()
        days_difference = (current_date - self.created_at).days
        if days_difference > 0 and current_date == self.last_studied_at :
            self.freshness += 1

    def update_last_studied(self) -> None:
        self.last_studied_at = datetime.now().date()

    def jsonify(self) -> str:
        """
        This method creates a json string with the object's data.
        :return: string representing the object in json.
        """
        return json.dumps({
            'ID': str(self.ID),  # Convert UUID to string
            'question': self.question,
            'answer': self.answer,
            'elo': self.elo,
            'freshness': self.freshness,
            'created_at': self.created_at,
            'last_studied_at': self.last_studied_at
        }, indent=2, default=str)