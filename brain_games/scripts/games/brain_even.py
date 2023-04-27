import random
from brain_games.engine.engine import game

yes: str = 'yes'
no: str = 'no'


def is_even(num: int) -> bool:
    return num % 2 == 0


def get_correct(correct_answer, answer):
    is_yes = answer == yes
    is_no = answer == no
    is_correct = (
            is_even(correct_answer) and is_yes
            or
            not is_even(correct_answer) and is_no
    )

    result = yes if is_even(correct_answer) else no

    return is_correct, result


def make_answer(question: tuple, answer):
    is_correct, result = get_correct(question[0], answer)

    return is_correct, result


def make_question() -> tuple:
    question = random.randint(1, 100)

    return (question,)


def main() -> None:
    game_name = 'brain-even'
    game_description = f"Answer \"{yes}\" if the number is even, " \
                       f"otherwise answer \"{no}\"."

    game(game_name, game_description, make_question, make_answer)


if __name__ == '__main__':
    main()
