import random
from brain_games.const import GCD_MIN, GCD_MAX


def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


def make_question():
    num1 = random.randint(GCD_MIN, GCD_MAX)
    num2 = random.randint(GCD_MIN, GCD_MAX)

    return (num1, num2), gcd(num1, num2)
