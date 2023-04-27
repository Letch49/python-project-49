import random
from brain_games.engine.engine import game

yes: str = 'yes'
no: str = 'no'


def check_prime(n, j=2):
    if n < 2:
        return False
    if j == n:
        return True
    if n % j == 0:
        return False
    return check_prime(n, j + 1)


def compute(num):
    return check_prime(num)


def get_correct(correct_answer, answer):
    is_yes = answer == yes
    is_no = answer == no

    is_correct = (
            correct_answer and is_yes
            or
            not correct_answer and is_no
    )

    result = yes if correct_answer else no

    return is_correct, result


def make_answer(question: tuple, answer):
    num = question[0]
    correct_answer = compute(num)

    is_correct, result = get_correct(correct_answer, answer)
    return is_correct, result


def make_question() -> tuple:
    num = random.randint(5, 7)

    return (num,)


def main() -> None:
    game_name = 'brain-prime'
    game_description = f"Answer {yes} if given number is prime. " \
                       f"Otherwise answer {no}."

    game(game_name, game_description, make_question, make_answer)


if __name__ == '__main__':
    main()
