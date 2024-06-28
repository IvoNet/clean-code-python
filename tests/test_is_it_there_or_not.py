#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import pytest

from is_it_there_or_not.is_it_there_or_not import Store, Customer, Product


@pytest.fixture(scope="function")
def setup():
    print("Setting up...")
    store = Store()
    store.delivery(Product("iPhone"))
    alice = Customer("Alice", Product("iPhone"))
    bob = Customer("Bob", Product("Samsung"))
    charlie = Customer("Charlie", Product("Coffee"))
    david = Customer("David", Product("iPhone"))
    eve = Customer("Eve", Product("sugar"))
    frank = Customer("Frank", Product("jam"))
    return store, {
        "alice": alice,
        "bob": bob,
        "charlie": charlie,
        "david": david,
        "eve": eve,
        "frank": frank,
    }


def test_1_customer_product_available(setup):
    store, customers = setup
    assert customers["alice"].go_shopping(store) is True
    assert customers["alice"].is_happy is True


def test_1_customer_product_not_available(setup):
    store, customers = setup
    assert customers["bob"].go_shopping(store) is False
    assert customers["bob"].is_happy is False


def test_observes_product_for_bob(setup):
    check_customer_product(setup, "bob", "Samsung")


def test_observes_product_for_charlie(setup):
    check_customer_product(setup, "charlie", "Coffee")


def test_observes_product_for_eve(setup):
    check_customer_product(setup, "eve", "sugar")


def test_observes_product_for_frank(setup):
    check_customer_product(setup, "frank", "jam")


def test_observes_product_for_david_alice_already_in_stock(setup):
    store, customers = setup
    assert customers["david"].go_shopping(store) is True
    assert customers["alice"].go_shopping(store) is True


def check_customer_product(setup, customer_name, product_name):
    store, customers = setup
    assert store.has_product(Product(product_name)) is False
    assert customers[customer_name].go_shopping(store) is False
    assert customers[customer_name].is_happy is False
    store.delivery(Product(product_name))
    assert store.has_product(Product(product_name)) is True
    assert customers[customer_name].is_happy is True
