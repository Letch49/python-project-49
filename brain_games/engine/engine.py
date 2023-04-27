import prompt


def _welcome(game_name: str, game_description: str) -> str:
    print(f'{game_name}\n')
    print('brain-games')
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game_description)

    return username


def _check_answer(answer, correct_answer, is_correct) -> bool:
    if is_correct:
        print("Correct!")
        return True

    print(
        f"'{answer}' is wrong answer ;(. Correct answer was ",
        f"'{correct_answer}'."
    )

    return False


def _play(username: str, make_question, make_answer, counter: int = 0) -> None:
    if counter == 3:
        print(f"Congratulations, {username}!")
        return

    question: tuple = make_question()
    print(f"Question: {' '.join([str(_) for _ in question])}")

    answer = prompt.string("Your answer: ")

    is_correct, correct_answer = make_answer(question, answer)

    if not _check_answer(answer, correct_answer, is_correct):
        print(f"Let's try again, {username}!")
        return

    _play(username, make_question, make_answer, counter + 1)


def game(game_name, game_description, make_question, make_answer):
    username = _welcome(game_name, game_description)

    _play(username, make_question, make_answer)
