import random
from brain_games.engine.engine import game
from brain_games.engine.const import (
    PROGRESSION_START_MIN,
    PROGRESSION_START_MAX,
    PROGRESSION_DIFF_MIN,
    PROGRESSION_DIF_MAX,
    PROGRESSION_N
)


def arithmetic_progression(start, diff, n):
    if n == 1:
        return [start]

    prev = arithmetic_progression(start, diff, n - 1)
    curr = prev[-1] + diff
    prev.append(curr)
    return prev


def make_question():
    start = random.randint(PROGRESSION_START_MIN, PROGRESSION_START_MAX)
    diff = random.randint(PROGRESSION_DIFF_MIN, PROGRESSION_DIF_MAX)
    n = PROGRESSION_N

    hidden_index = random.randint(0, n - 1)

    result = arithmetic_progression(start, diff, n)

    correct_value = result[hidden_index]
    result[hidden_index] = '..'

    return {
        'question_values': tuple(result),
        'correct_value': correct_value
    }


def main():
    game_name = 'brain-progression'
    game_description = "What number is missing in the progression?"

    game(game_name, game_description, make_question)


if __name__ == '__main__':
    main()
