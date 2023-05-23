import prompt
from brain_games.const import GAME_COUNTER


def _play(username: str, make_question, counter: int = 0) -> None:
    if counter == GAME_COUNTER:
        print(f"Congratulations, {username}!")
        return

    values, correct_answer = make_question()

    print(f"Question: {' '.join([str(_) for _ in values])}")

    answer = prompt.string("Your answer: ")

    if answer == correct_answer:
        print('Correct')
    else:
        print(
            f"'{answer}' is wrong answer ;(. Correct answer was ",
            f"'{correct_answer}'."
        )
        print(f"Let's try again, {username}!")
        return

    _play(username, make_question, counter + 1)


def game(game_name, game_description, make_question):
    print(f'{game_name}\n')
    print('brain-games')
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game_description)

    _play(username, make_question)
