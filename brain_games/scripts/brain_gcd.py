from brain_games.engine import game
from brain_games.games.brain_gcd import make_question
from brain_games.const import GCD_GAME_NAME, GCD_GAME_DESCRIPTION


def main():
    game(GCD_GAME_NAME, GCD_GAME_DESCRIPTION, make_question)


if __name__ == '__main__':
    main()
