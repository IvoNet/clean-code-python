#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


import pytest

from doors_will_be_doors.doors_will_be_doors import (
    Door,
    OpenDoor,
    ClosingDoor,
    OpeningDoor,
    ClosedDoor,
)


def test_open_door():
    door = Door()
    door.state = OpenDoor()
    assert isinstance(door.state, OpenDoor)
    with pytest.raises(
        Exception, match="The door cannot be opened while it's already open"
    ):
        door.open()
    door.enter()


def test_opening_door():
    door = Door()
    door.open()
    assert isinstance(door.state, OpeningDoor)
    with pytest.raises(Exception, match="You can't enter while the door is opening"):
        door.enter()


def test_entering_closed_door():
    door = Door()
    door.state = ClosedDoor()
    assert isinstance(door.state, ClosedDoor)
    with pytest.raises(Exception, match="The door is closed, you can't enter"):
        door.enter()


def test_closing_door():
    door = Door()
    door.state = ClosingDoor()
    assert isinstance(door.state, ClosingDoor)
    with pytest.raises(Exception, match="You can't enter while the door is closing"):
        door.enter()


def test_opening_a_closed_door():
    door = Door()
    door.open()
    assert isinstance(door.state, OpeningDoor)
    with pytest.raises(Exception, match="You can't enter while the door is opening"):
        door.enter()
    with pytest.raises(Exception, match="You can't exit while the door is opening"):
        door.exit()
    with pytest.raises(Exception, match="The door is already opening..."):
        door.open()
