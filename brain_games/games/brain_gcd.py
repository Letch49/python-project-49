import random
from brain_games.const import GCD_MIN, GCD_MAX


def calculate_gcd(num1, num2):
    if num2 == 0:
        return num1
    return calculate_gcd(num2, num1 % num2)


def make_question():
    num1 = random.randint(GCD_MIN, GCD_MAX)
    num2 = random.randint(GCD_MIN, GCD_MAX)

    question = (num1, num2)
    answer = str(calculate_gcd(num1, num2))

    return question, answer
