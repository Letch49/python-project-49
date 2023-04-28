import random
from brain_games.engine.engine import game
from brain_games.engine.const import (
    YES,
    NO,
    PRIME_START_MIN,
    PRIME_START_MAX
)


def check_prime(n, j=2):
    if n < 2:
        return False
    if j == n:
        return True
    if n % j == 0:
        return False
    return check_prime(n, j + 1)


def make_question():
    num = random.randint(PRIME_START_MIN, PRIME_START_MAX)

    return {
        'question_values': (num,),
        'correct_value': YES if check_prime(num) else NO
    }


def main():
    game_name = 'brain-prime'
    game_description = f"Answer {YES} if given number is prime. " \
                       f"Otherwise answer {NO}."

    game(game_name, game_description, make_question)


if __name__ == '__main__':
    main()
