import random
from brain_games.engine.engine import game


def compute(num1, num2):
    if num2 == 0:
        return num1
    return compute(num2, num1 % num2)


def get_correct(correct_answer, answer):
    return str(answer) == str(correct_answer), correct_answer


def make_answer(question: tuple, answer):
    num1, num2 = question
    correct_answer = compute(int(num1), int(num2))

    is_correct, result = get_correct(correct_answer, answer)
    return is_correct, result


def make_question() -> tuple:
    num1, num2 = random.randint(1, 100), random.randint(1, 100)

    return num1, num2


def main() -> None:
    game_name = 'brain-gcd'
    game_description = "Find the greatest common divisor of given numbers."

    game(game_name, game_description, make_question, make_answer)


if __name__ == '__main__':
    main()
