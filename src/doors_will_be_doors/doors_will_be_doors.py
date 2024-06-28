#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


# Define the abstract state class
class DoorState(ABC):
    @abstractmethod
    def enter(self) -> str:
        pass

    @abstractmethod
    def exit(self) -> str:
        pass

    @abstractmethod
    def close(self) -> "DoorState":
        pass

    @abstractmethod
    def open(self) -> "DoorState":
        pass


# Concrete states: Open, Opening, Closed, and Closing
class OpenDoor(DoorState):
    def enter(self):
        return "entered"

    def exit(self):
        return "exited"

    def close(self):
        return ClosingDoor()

    def open(self):
        raise Exception("The door cannot be opened while it's already open")


class OpeningDoor(DoorState):
    def enter(self):
        raise Exception("You can't enter while the door is opening")

    def exit(self):
        raise Exception("You can't exit while the door is opening")

    def close(self):
        return ClosingDoor()

    def open(self):
        raise Exception("The door is already opening...")


class ClosedDoor(DoorState):
    def enter(self):
        raise Exception("The door is closed, you can't enter")

    def exit(self):
        raise Exception("The door is closed, you can't exit")

    def close(self):
        raise Exception("The door is already closed...")

    def open(self):
        return OpeningDoor()


class ClosingDoor(DoorState):
    def enter(self):
        raise Exception("You can't enter while the door is closing")

    def exit(self):
        raise Exception("You can't exit while the door is closing")

    def close(self):
        pass

    def open(self):
        print("The door is opening...")
        return OpeningDoor()


# Context: Door
class Door:
    def __init__(self):
        self.state = ClosedDoor()

    def enter(self):
        self.state.enter()

    def exit(self):
        self.state.exit()
        self.state = ClosedDoor()  # Transition to the new state

    def close(self):
        self.state = self.state.close()

    def open(self):
        self.state = self.state.open()


if __name__ == "__main__":
    door = Door()
    print("Initial state: ", door.state.__class__.__name__)
    door.enter()
    print("After entering:", door.state.__class__.__name__)
    door.exit()
    print("After exiting:", door.state.__class__.__name__)
    door.close()
    print("After closing:", door.state.__class__.__name__)
    door.open()
    print("After opening:", door.state.__class__.__name__)
