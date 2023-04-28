import prompt
from brain_games.engine.const import GAME_COUNTER


def _welcome(game_name: str, game_description: str) -> str:
    print(f'{game_name}\n')
    print('brain-games')
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game_description)

    return username


def _check_answer(answer, correct_answer) -> bool:
    if answer == correct_answer:
        print("Correct!")
        return True

    print(
        f"'{answer}' is wrong answer ;(. Correct answer was ",
        f"'{correct_answer}'."
    )

    return False


def _play(username: str, make_question, counter: int = 0) -> None:
    if counter == GAME_COUNTER:
        print(f"Congratulations, {username}!")
        return

    question_result = make_question()
    values = question_result['question_values']
    correct_answer = str(question_result['correct_value'])

    print(f"Question: {' '.join([str(_) for _ in values])}")

    answer = prompt.string("Your answer: ")

    if not _check_answer(answer, correct_answer):
        print(f"Let's try again, {username}!")
        return

    _play(username, make_question, counter + 1)


def game(game_name, game_description, make_question):
    username = _welcome(game_name, game_description)

    _play(username, make_question)
