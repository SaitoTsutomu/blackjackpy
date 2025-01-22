# flake8: noqa: S101 D100
import unittest.mock
from collections.abc import Callable
from textwrap import dedent

import pytest
from more_itertools import repeat_last

from blackjackpy import GameMaster, Player


def ask(player_answers: str) -> Callable[[Player], str]:
    """Player.askのモック

    player_answersの各文字を順番に返す。最後の文字を繰り返す
    """
    answers = repeat_last(player_answers)
    return lambda _cls: next(answers)


expected1 = """\
    Player(19):  J(D) 9(D)
    Dealer(--):  Q(D) *(*)
    Player(20):  J(D) 9(D) A(D)
    Dealer(--):  Q(D) *(*)
    Player(20):  J(D) 9(D) A(D)
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
    Dealer(17):  Q(D) 7(D)
    You win.
"""
expected4 = """\
    Player(20):  J(D) K(D)
    Dealer(--):  Q(D) *(*)
    Player(20):  J(D) K(D)
    Dealer(21):  Q(D) 6(D) 5(D)
    You lose.
"""
expected5 = """\
    Player(20):  J(D) K(D)
    Dealer(--):  Q(D) *(*)
    Player(21):  J(D) K(D) A(D)
    Dealer(21):  Q(D) 6(D) 5(D)
    Draw.
"""


@pytest.mark.parametrize(
    ("cards", "player_answers", "expected"),
    [
        ([10, 11, 8, 8, 0], "yn", dedent(expected1)),
        ([10, 11, 12, 8, 0], "y", dedent(expected2)),
        ([10, 11, 12, 6], "n", dedent(expected3)),
        ([10, 11, 12, 5, 4], "n", dedent(expected4)),
        ([10, 11, 12, 5, 0, 4], "yn", dedent(expected5)),
    ],
)
def test_game(capsys, cards: list[int], player_answers: str, expected: str):
    """ゲームのテスト

    :param capsys: 標準入力用フィクスチャ
    :param cards: 配布されるカードのリスト
    :param player_answers: プレイヤーの選択
    :param expected: 期待する標準出力
    """
    gm = GameMaster(cards=cards)
    with unittest.mock.patch("blackjackpy.Player.ask", new=ask(player_answers)):
        gm.start_game()
    captured = capsys.readouterr()
    assert captured.out == expected
