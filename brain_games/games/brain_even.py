import random
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
