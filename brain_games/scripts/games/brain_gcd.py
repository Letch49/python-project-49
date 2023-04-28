import random
from brain_games.engine.engine import game
from brain_games.engine.const import GCD_MIN, GCD_MAX


def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


def make_question():
    num1 = random.randint(GCD_MIN, GCD_MAX)
    num2 = random.randint(GCD_MIN, GCD_MAX)

    return {
        'question_values': (num1, num2),
        'correct_value': gcd(num1, num2)
    }


def main():
    game_name = 'brain-gcd'
    game_description = "Find the greatest common divisor of given numbers."

    game(game_name, game_description, make_question)


if __name__ == '__main__':
    main()
