from brain_games.games.brain_calc import make_question
from brain_games.engine import game
from brain_games.const import CALC_GAME_NAME, CALC_GAME_DESCRIPTION


def main():
    game(CALC_GAME_NAME, CALC_GAME_DESCRIPTION, make_question)


if __name__ == '__main__':
    main()
