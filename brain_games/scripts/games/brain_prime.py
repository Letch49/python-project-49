from brain_games.engine.const import YES, NO
from brain_games.engine.engine import game
from brain_games.games.brain_prime import make_question


def main():
    game_name = 'brain-prime'
    game_description = f"Answer \"{YES}\" if given number is prime. " \
                       f"Otherwise answer \"{NO}\"."

    game(game_name, game_description, make_question)


if __name__ == '__main__':
    main()
