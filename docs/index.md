# About Blackjack

## Objective

Having a higher sum than the dealer's hand.

## Card Values

* Numeric cards (2-10): The value is as indicated by the number shown.
* Face cards (Jack, Queen, King): Each has a value of 10.
* Ace: Can be set to either 1 or 11.

## Game Flow

* Deal the cards
  * The player and the dealer are each dealt two cards. The player's cards are both face up, while the dealer's is one face up and the other face down.
* Player's Choice
  * Hit: Draw another card.
  * Stand: Play with the current hand.
* Dealer's Turn
  * The dealer turns the face-down cards face up and draws cards until he has 17 or more.
* Winner Decides
  * If the total hand exceeds 21, then loses on a “bust”.
  * When the dealer busts, the remaining player wins.
  * If the hand is high, then wins.
  * If the hands are the same, then tie.

## Install

```sh
pip install blackjackpy
```

## How to play

```sh
$ blackjackpy
Player( 6):  2(C) 4(S)
Dealer(--):  5(C) *(*)
Hit? (y/n) y
Player(16):  2(C) 4(S) J(C)
Dealer(--):  5(C) *(*)
Hit? (y/n) n
Player(16):  2(C) 4(S) J(C)
Dealer(17):  5(C) 3(C) 9(S)
You lose.
```

```sh
$ blackjackpy
Player(20): 10(S) K(C)
Dealer(--):  7(C) *(*)
Hit? (y/n) n
Player(20): 10(S) K(C)
Dealer(18):  7(C) A(H)
You win.
```
