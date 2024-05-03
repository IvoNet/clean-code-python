#!/usr/bin/env python3
#  -*- coding: utf-8 -*
import functools
import unittest


class Singleton:
    """Singleton. This code demonstrates how to make a class into a singleton."""
    _instance = None  # Class-level attribute to store the single instance

    def __new__(cls: 'Singleton') -> 'Singleton':
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


def singleton(cls):
    """Decorator function - Make a class a Singleton class"""

    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        """wrapper function for the singleton decorator."""
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class SingletonDecorator:
    """This class is now a singleton as done by the decorator"""
    the_answer = 42


class UnitTests(unittest.TestCase):
    def test_both_instances_of_the_singleton_are_equal(self):
        s1 = Singleton()
        s2 = Singleton()
        s1.foo = 42
        self.assertEqual(s1, s2)
        # note that s2.foo was never set, but it does exist because s1 and s2 refer to the same object
        self.assertEqual(s1.foo, s2.foo)

    def test_both_instances_of_the_decorated_singleton_are_the_same_object(self):
        s1 = SingletonDecorator()
        s2 = SingletonDecorator()
        s2.the_answer = 43
        self.assertEqual(s1, s2)
        self.assertEqual(s1.the_answer, s2.the_answer)


if __name__ == '__main__':
    unittest.main()
