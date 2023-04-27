import random
from brain_games.engine.engine import game

plus = '+'
minus = '-'
multiply = '*'


def get_operation(operations: tuple = (plus, minus, multiply)) -> str:
    return random.choice(operations)


def compute(num1: int, num2: int, operation) -> int:
    if operation == plus:
        return num1 + num2
    elif operation == minus:
        return num1 - num2
    elif operation == multiply:
        return num1 * num2


def get_correct(correct_answer, answer):
    return str(answer) == str(correct_answer), correct_answer


def make_answer(question, answer):
    num1, operation, num2 = question

    correct_answer = compute(int(num1), int(num2), operation)
    is_correct, result = get_correct(correct_answer, answer)

    return is_correct, result


def make_question() -> tuple:
    operation = get_operation()
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    return num1, operation, num2


def main() -> None:
    game_name = 'brain-even'
    game_description = "What is the result of the expression?"

    game(game_name, game_description, make_question, make_answer)


if __name__ == '__main__':
    main()
