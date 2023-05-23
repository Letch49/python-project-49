import random
from brain_games.const import (
    YES,
    NO,
    EVEN_MIN,
    EVEN_MAX
)


def is_even(num: int):
    return num % 2 == 0


def make_question():
    result = random.randint(EVEN_MIN, EVEN_MAX)

    question = (result,)
    answer = YES if is_even(result) else NO

    return question, answer
