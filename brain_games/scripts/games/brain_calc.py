from brain_games.games.brain_calc import make_question
from brain_games.engine.engine import game


def main():
    game_name = 'brain-even'
    game_description = "What is the result of the expression?"

    game(game_name, game_description, make_question)


if __name__ == '__main__':
    main()
