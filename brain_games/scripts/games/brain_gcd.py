from brain_games.engine.engine import game
from brain_games.games.brain_gcd import make_question


def main():
    game_name = 'brain-gcd'
    game_description = "Find the greatest common divisor of given numbers."

    game(game_name, game_description, make_question)


if __name__ == '__main__':
    main()
