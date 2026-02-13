import pytest


@pytest.fixture
def game():
    return RPS()


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


# =========================
# PAPER/PAPEL GANA O PIERDE
# =========================

@pytest.mark.paper
def test_paper_wins(game):
    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.ROCK)


@pytest.mark.paper
def test_paper_loses(game):
    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.SCISSORS)


# =========================
# SCISSORS/TIJERAS GANA O PIERDE
# =========================

@pytest.mark.scissors
def test_scissors_wins(game):
    assert GameResult.VICTORY == game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.PAPER)


@pytest.mark.scissors
def test_scissors_loses(game):
    assert GameResult.DEFEAT == game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.ROCK)
