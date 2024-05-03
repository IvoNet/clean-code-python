#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

# TODO NOTE!!! niet goede code (yet)

import random
from abc import ABC, abstractmethod
from typing import Protocol

STATES = ["Win", "Lose", "Tie"]


class TieCondition(Protocol):
    def ties(self, other: "Strategy") -> bool:
        return self == other


# create a protocol for the win condition for the strategy implementations
class WinCondition(Protocol):
    @abstractmethod
    def wins(self, other: "Strategy") -> bool:
        raise NotImplementedError


class Strategy(ABC, WinCondition, TieCondition):
    @abstractmethod
    def selection(self) -> None:
        ...


class Rock(Strategy):
    def selection(self) -> str:
        return "Rock"

    def wins(self, other: Strategy) -> bool:
        return isinstance(other, Scissors)


class Paper(Strategy):
    def selection(self) -> str:
        return "Paper"

    def wins(self, other: Strategy) -> bool:
        return isinstance(other, Rock)


class Scissors(Strategy):
    def selection(self) -> str:
        return "Scissors"

    def wins(self, other: Strategy) -> bool:
        return isinstance(other, Paper)


class Random(Strategy):
    def selection(self) -> str:
        options = ["Rock", "Paper", "Scissors"]
        return random.choice(options)

    def wins(self, other: Strategy) -> bool:
        if self.selection() == "Rock":
            return isinstance(other, Scissors)
        elif self.selection() == "Paper":
            return isinstance(other, Rock)
        elif self.selection() == "Scissors":
            return isinstance(other, Paper)


## Context class
class Game:
    strategy: Strategy

    def __init__(self, strategy: Strategy = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Random()

    def play(self, sec) -> None:
        s1 = self.strategy.selection()
        s2 = sec.strategy.selection()
        if s1 == s2:
            print("It's a tie")
        else:
            if s1.wins(s2):
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")


if __name__ == '__main__':
    ## Example application
    ## PLayer 1 can select his strategy
    player1 = Game(Paper())

    # Player 2 gets to select
    player2 = Game(Rock())

    # After the second player choice, we call the play method
    player1.play(player2)
