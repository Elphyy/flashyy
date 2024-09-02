from src.models.flashcard import Flashcard


def main():
    card = Flashcard("what is the first day of the year?", "1st of January")
    card_json = card.jsonify()
    print(card_json)


if __name__ == '__main__':
    main()