import random
import typing

POINT21: typing.Final[int] = 21


class Card:
    """カード"""

    def __init__(self, num: int):
        self.suit = num // 13 + 1
        self.rank = num % 13 + 1

    def point(self) -> int:
        return min(10, self.rank)

    def __str__(self):
        n = self.rank * 2
        m = n - 2
        r = " A 2 3 4 5 6 7 8 910 J Q K"[m:n]
        s = "(" + "DHSC"[self.suit - 1] + ")"
        return r + s


class Owner:
    """手札を持ち、カードを引ける人"""

    def __init__(self):
        self.hands = []

    def draw(self, gm: "GameMaster") -> None:
        self.hands.append(gm.pop())

    def sequence(self, *, hidden: bool = False) -> str:
        s = "".join(str(cd) for cd in self.hands)
        return (s[:5] + " *(*)" + s[10:]) if hidden else s

    def point(self) -> int:
        pnt = sum(cd.point() for cd in self.hands)
        for cd in self.hands:
            if cd.rank == 1 and pnt + 10 <= POINT21:
                pnt += 10
        return pnt


class Player(Owner):
    """プレイヤー"""

    @classmethod
    def ask(cls) -> str:
        print("Hit? (y/n) ", end="")
        return input()

    def act(self, gm: "GameMaster") -> None:
        while self.point() < POINT21:
            gm.show(hidden=True)
            answer = ""
            while answer not in {"y", "n"}:
                answer = self.ask()
            if answer == "n":
                break
            self.draw(gm)


class Dealer(Owner):
    """ディーラー"""

    LOWER: typing.Final[int] = 17

    def act(self, gm: "GameMaster") -> None:
        while self.point() < self.LOWER:
            self.draw(gm)


class GameMaster:
    """ゲームマスター"""

    def __init__(self, seed: int | None = None, *, cards: list[int] | None = None):
        if cards:
            self.cards = [Card(i) for i in cards]
        else:
            self.cards = [Card(i) for i in range(52)]
            if seed is not None:
                random.seed(seed)
            random.shuffle(self.cards)
        self.player = Player()
        self.dealer = Dealer()

    def start_game(self) -> None:
        for _ in range(2):
            self.player.draw(self)
            self.dealer.draw(self)
        self.player.act(self)
        player_point = self.player.point()
        self.message = "You lose."
        if player_point <= POINT21:
            self.dealer.act(self)
            dealer_point = self.dealer.point()
            if player_point == dealer_point:
                self.message = "Draw."
            elif dealer_point > POINT21 or dealer_point < player_point:
                self.message = "You win."
        self.show(hidden=False)
        print(self.message)

    def show(self, *, hidden: bool) -> None:
        player_point = self.player.point()
        player_sequence = self.player.sequence()
        print(f"Player({player_point:2}): {player_sequence}")
        dealer_point = "--" if hidden else self.dealer.point()
        dealer_sequence = self.dealer.sequence(hidden=hidden)
        print(f"Dealer({dealer_point:2}): {dealer_sequence}")

    def pop(self) -> Card:
        return self.cards.pop(0)


def main():
    GameMaster().start_game()
