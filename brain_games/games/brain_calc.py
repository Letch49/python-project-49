import random
from brain_games.const import (
    PLUS,
    MINUS,
    MULTIPLY,
    CALC_START_MIN,
    CALC_START_MAX
)


def calculate_operation(num1, num2, operation):
    if operation == PLUS:
        return num1 + num2
    elif operation == MINUS:
        return num1 - num2
    elif operation == MULTIPLY:
        return num1 * num2


def make_question():
    operation = random.choice((PLUS, MINUS, MULTIPLY))
    num1 = random.randint(CALC_START_MIN, CALC_START_MAX)
    num2 = random.randint(CALC_START_MIN, CALC_START_MAX)

    question = (num1, operation, num2)
    answer = str(calculate_operation(num1, num2, operation))

    return question, answer
