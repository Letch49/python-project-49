import random
from brain_games.const import (
    YES,
    NO,
    PRIME_START_MIN,
    PRIME_START_MAX
)


def is_prime(n, j=2):
    if n < 2:
        return False
    if j == n:
        return True
    if n % j == 0:
        return False
    return is_prime(n, j + 1)


def make_question():
    result = random.randint(PRIME_START_MIN, PRIME_START_MAX)

    question = (result,)
    answer = YES if is_prime(result) else NO

    return question, answer
