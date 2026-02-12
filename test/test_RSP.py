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

