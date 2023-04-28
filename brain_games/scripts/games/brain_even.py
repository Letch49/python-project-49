import random
from brain_games.engine.engine import game
from brain_games.engine.const import (
    YES,
    NO,
    EVEN_MIN,
    EVEN_MAX
)


def is_even(num: int) -> bool:
    return num % 2 == 0


def make_question():
    question = random.randint(EVEN_MIN, EVEN_MAX)

    return {
        'question_values': (question,),
        'correct_value': YES if is_even(question) else NO
    }


def main() -> None:
    game_name = 'brain-even'
    game_description = f"Answer \"{YES}\" if the number is even, " \
                       f"otherwise answer \"{NO}\"."

    game(game_name, game_description, make_question)


if __name__ == '__main__':
    main()
