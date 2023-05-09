from brain_games.engine.const import YES, NO
from brain_games.engine.engine import game
from brain_games.games.brain_even import make_question


def main() -> None:
    game_name = 'brain-even'
    game_description = f"Answer \"{YES}\" if the number is even, " \
                       f"otherwise answer \"{NO}\"."

    game(game_name, game_description, make_question)


if __name__ == '__main__':
    main()
