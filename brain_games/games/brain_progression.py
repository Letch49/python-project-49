import random
from brain_games.const import (
    PROGRESSION_START_MIN,
    PROGRESSION_START_MAX,
    PROGRESSION_DIFF_MIN,
    PROGRESSION_DIF_MAX,
    PROGRESSION_N
)


def calculate_arithmetic_progression(start, diff, n):
    if n == 1:
        return [start]

    prev = calculate_arithmetic_progression(start, diff, n - 1)
    curr = prev[-1] + diff
    prev.append(curr)
    return prev


def make_question():
    start = random.randint(PROGRESSION_START_MIN, PROGRESSION_START_MAX)
    diff = random.randint(PROGRESSION_DIFF_MIN, PROGRESSION_DIF_MAX)
    n = PROGRESSION_N

    hidden_index = random.randint(0, n - 1)

    result = calculate_arithmetic_progression(start, diff, n)

    value = result[hidden_index]
    result[hidden_index] = '..'

    question = tuple(result)
    answer = str(value)

    return question, answer
