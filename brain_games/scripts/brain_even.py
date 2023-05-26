from brain_games.const import EVEN_GAME_NAME, EVEN_GAME_DESCRIPTION
from brain_games.engine import make_game
from brain_games.games.brain_even import make_question


def main():
    make_game(EVEN_GAME_NAME, EVEN_GAME_DESCRIPTION, make_question)


if __name__ == '__main__':
    main()
