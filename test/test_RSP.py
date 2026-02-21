import pytest
from src.RPS_dict import GameAction, GameResult, RPS


@pytest.fixture
def game():
    return RPS()


# =========================
# DRAW/EMPATES
# =========================

@pytest.mark.draw
def test_draw(game):
    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Rock)

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Paper)

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Scissors)


# =========================
# ROCK/PIEDRA GANA O PIERDE
# =========================

@pytest.mark.rock
def test_rock_wins(game):
    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Scissors)


@pytest.mark.rock
def test_rock_loses(game):
    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Paper)


# =========================
# PAPER/PAPEL GANA O PIERDE
# =========================

@pytest.mark.paper
def test_paper_wins(game):
    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Rock)


@pytest.mark.paper
def test_paper_loses(game):
    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Scissors)


# =========================
# SCISSORS/TIJERAS GANA O PIERDE
# =========================

@pytest.mark.scissors
def test_scissors_wins(game):
    assert GameResult.Victory == game.assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Paper)


@pytest.mark.scissors
def test_scissors_loses(game):
    assert GameResult.Defeat == game.assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Rock)
