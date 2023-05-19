import random
from brain_games.const import (
    YES,
    NO,
    EVEN_MIN,
    EVEN_MAX
)


def is_even(num: int) -> bool:
    return num % 2 == 0


def make_question():
    question = random.randint(EVEN_MIN, EVEN_MAX)

    return (question,), YES if is_even(question) else NO
