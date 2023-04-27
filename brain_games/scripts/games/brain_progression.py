import random
from brain_games.engine.engine import game


def arithmetic_progression(start, diff, n):
    if n == 1:
        return [start]
    else:
        prev = arithmetic_progression(start, diff, n - 1)
        curr = prev[-1] + diff
        prev.append(curr)
        return prev


def get_correct(correct_answer, answer):
    return str(answer) == str(correct_answer), correct_answer


def compute(numbers: tuple):
    hidden_index = numbers.index('..')

    diff = None

    if hidden_index > 2:
        diff = numbers[hidden_index - 1] - numbers[hidden_index - 2]
    else:
        diff = numbers[hidden_index + 2] - numbers[hidden_index + 1]

    if hidden_index == 0:
        return numbers[hidden_index + 1] - diff

    return numbers[hidden_index - 1] + diff


def make_answer(numbers: tuple, answer):
    correct_answer = compute(numbers)

    is_correct, result = get_correct(correct_answer, answer)
    return is_correct, result


def make_question() -> tuple:
    start = random.randint(1, 20)
    diff = random.randint(1, 10)
    n = 10

    hidden_index = random.randint(0, n - 1)

    result = arithmetic_progression(start, diff, n)

    result[hidden_index] = '..'

    return tuple(result)


def main() -> None:
    game_name = 'brain-progression'
    game_description = "What number is missing in the progression?"

    game(game_name, game_description, make_question, make_answer)


if __name__ == '__main__':
    main()
