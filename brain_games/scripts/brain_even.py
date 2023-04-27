import random
import prompt


def welcome_user() -> str:
    print('brain-games')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    return name


yes: str = 'yes'
no: str = 'no'


def is_even(num: int) -> bool:
    return num % 2 == 0


def check_answer(number, answer) -> bool:
    is_yes = answer == yes
    is_no = answer == no

    if is_even(number) and is_yes or not is_even(number) and is_no:
        print("Correct!")
        return True

    print(
        f"'{answer}' is wrong answer ;(. Correct answer was ",
        f"'{yes if is_even(number) else no}'."
    )
    return False


def play(username: str, counter: int = 0) -> None:
    if counter == 3:
        print(f"Congratulations, {username}!")
        return

    question = random.randint(1, 100)

    print(f"Question: {question}")

    answer = prompt.string("Your answer: ").lower()

    if not check_answer(question, answer):
        return

    play(username, counter + 1)


def main() -> None:
    print('brain-even\n')
    username = welcome_user()
    print(f"Answer \"{yes}\" if the number is even, otherwise answer \"{no}\".")

    play(username, 0)


if __name__ == '__main__':
    main()
