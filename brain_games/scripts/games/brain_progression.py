from brain_games.engine.engine import game
from brain_games.games.brain_progression import make_question


def main():
    game_name = 'brain-progression'
    game_description = "What number is missing in the progression?"

    game(game_name, game_description, make_question)


if __name__ == '__main__':
    main()
