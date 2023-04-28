import random
from brain_games.engine.engine import game
from brain_games.engine.const import (
    PLUS,
    MINUS,
    MULTIPLY,
    CALC_START_MIN,
    CALC_START_MAX
)


def get_operation(operations: tuple = (PLUS, MINUS, MULTIPLY)) -> str:
    return random.choice(operations)


def get_math_result(num1: int, num2: int, operation) -> int:
    if operation == PLUS:
        return num1 + num2
    elif operation == MINUS:
        return num1 - num2
    elif operation == MULTIPLY:
        return num1 * num2


def make_question():
    operation = get_operation()
    num1 = random.randint(CALC_START_MIN, CALC_START_MAX)
    num2 = random.randint(CALC_START_MIN, CALC_START_MAX)

    return {
        'question_values': (num1, operation, num2),
        'correct_value': get_math_result(num1, num2, operation)
    }


def main():
    game_name = 'brain-even'
    game_description = "What is the result of the expression?"

    game(game_name, game_description, make_question)


if __name__ == '__main__':
    main()
