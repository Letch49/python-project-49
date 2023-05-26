from brain_games.engine import make_game
from brain_games.games.brain_progression import make_question
from brain_games.const import (
    PROGRESSION_GAME_NAME,
    PROGRESSION_GAME_DESCRIPTION
)


def main():
    make_game(
        PROGRESSION_GAME_NAME,
        PROGRESSION_GAME_DESCRIPTION,
        make_question
    )


if __name__ == '__main__':
    main()
