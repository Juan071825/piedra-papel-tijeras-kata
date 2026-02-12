import pytest

@pytest.fixture
def game():
    return Game()


# =========================
# DRAW/EMPATES
# =========================

@pytest.mark.draw
def test_draw(game):
    assert GameResult.TIE == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.ROCK)

    assert GameResult.TIE == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.PAPER)

    assert GameResult.TIE == game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.SCISSORS)


# =========================
# ROCK/PIEDRA GANA O PIERDE
# =========================

@pytest.mark.rock
def test_rock_wins(game):
    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.SCISSORS)


@pytest.mark.rock
def test_rock_loses(game):
    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.PAPER)


