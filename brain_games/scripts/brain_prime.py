from brain_games.const import PRIME_GAME_NAME, PRIME_GAME_DESCRIPTION
from brain_games.engine import game
from brain_games.games.brain_prime import make_question


def main():
    game(PRIME_GAME_NAME, PRIME_GAME_DESCRIPTION, make_question)


if __name__ == '__main__':
    main()
