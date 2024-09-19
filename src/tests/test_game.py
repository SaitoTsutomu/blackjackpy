from textwrap import dedent

import pytest
from more_itertools import repeat_last

from blackjackpy import GameMaster


def ask(player_answers: str):
    return lambda: next(repeat_last(player_answers))


expected1 = """\
    Player(20):  J(D) K(D)
    Dealer(--):  Q(D) *(*)
    Player(20):  J(D) K(D)
    Dealer(19):  Q(D) 9(D)
    You win.
"""
expected2 = """\
    Player(20):  J(D) K(D)
    Dealer(--):  Q(D) *(*)
    Player(21):  J(D) K(D) A(D)
    Dealer(19):  Q(D) 9(D)
    You win.
"""
expected3 = """\
    Player(20):  J(D) K(D)
    Dealer(--):  Q(D) *(*)
    Player(20):  J(D) K(D)
    Dealer(21):  Q(D) 6(D) 5(D)
    You lose.
"""
expected4 = """\
    Player(20):  J(D) K(D)
    Dealer(--):  Q(D) *(*)
    Player(21):  J(D) K(D) A(D)
    Dealer(21):  Q(D) 6(D) 5(D)
    Draw.
"""


@pytest.mark.parametrize(
    ("cards", "player_answers", "expected"),
    [
        ([10, 11, 12, 8], "n", dedent(expected1)),
        ([10, 11, 12, 8, 0], "yn", dedent(expected2)),
        ([10, 11, 12, 5, 4], "n", dedent(expected3)),
        ([10, 11, 12, 5, 0, 4], "yn", dedent(expected4)),
    ],
)
def test_game(capsys, cards, player_answers, expected):
    gm = GameMaster(cards=cards)
    gm.player.ask = ask(player_answers)
    gm.start_game()
    captured = capsys.readouterr()
    assert captured.out == expected
