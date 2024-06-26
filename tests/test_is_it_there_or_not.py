#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import threading
import time

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
    assert store.has_product(Product("iPhone")) is True
    assert customers["alice"].go_shopping(store) is True


def test_1_customer_product_not_available(setup):
    store, customers = setup
    assert store.has_product(Product("Samsung")) is False
    assert customers["bob"].go_shopping(store) is False


def test_customer_keep_checking(setup):
    store, customers = setup
    customers_go_to_store = CustomersGoToStoreToAskForProduct(
        store, list(customers.values())
    )
    customers_go_to_store.start()
    try:
        assert customers_go_to_store.customers_satisfied() is False
        assert customers_go_to_store.customer_satisfied(customers["alice"]) is True
        assert customers_go_to_store.customer_satisfied(customers["david"]) is True

        assert customers_go_to_store.customer_satisfied(customers["bob"]) is False
        customers_go_to_store.deliver_product(Product("Samsung"))
        assert customers_go_to_store.customer_satisfied(customers["bob"]) is True

        assert customers_go_to_store.customer_satisfied(customers["charlie"]) is False
        customers_go_to_store.deliver_product(Product("Coffee"))
        assert customers_go_to_store.customer_satisfied(customers["charlie"]) is True

        assert customers_go_to_store.customer_satisfied(customers["eve"]) is False
        customers_go_to_store.deliver_product(Product("sugar"))
        assert customers_go_to_store.customer_satisfied(customers["eve"]) is True

        assert customers_go_to_store.customer_satisfied(customers["frank"]) is False
        customers_go_to_store.deliver_product(Product("jam"))
        assert customers_go_to_store.customer_satisfied(customers["frank"]) is True

        assert customers_go_to_store.customers_satisfied() is True
    finally:
        customers_go_to_store.stop()


class CustomersGoToStoreToAskForProduct:
    def __init__(self, store: Store, customers: list[Customer]):
        self.store = store
        self.customers = customers
        self.threads = {}
        self.found = {customer.name: False for customer in self.customers}

    def customer_thread(self, customer: Customer):
        while not self.threads[customer.name].stopped:
            time.sleep(0.1)
            if customer.go_shopping(self.store):
                self.found[customer.name] = True
                print(
                    f"[FOUND] {customer.name} has found the {customer.product_of_interest}."
                )
                break
            self.found[customer.name] = False
            print(
                f"[NOT FOUND] {customer.name} has not found the {customer.product_of_interest} yet."
            )

    def deliver_product(self, product_name):
        self.store.delivery(product_name)
        time.sleep(0.2)

    def customers_satisfied(self):
        for customer in self.customers:
            if customer.go_shopping(self.store):
                self.found[customer.name] = True
        return all(self.found.values())

    def customer_satisfied(self, customer: Customer):
        return self.found[customer.name]

    def start(self):
        for customer in self.customers:
            # noinspection PyTypeChecker
            thread = StoppableThread(target=self.customer_thread, args=(customer,))
            self.threads[customer.name] = thread
            thread.start()

    def stop(self):
        for thread in self.threads.values():
            thread.stop()
        print("All threads stopped.")


class StoppableThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self.__stop: bool = False

    def stop(self):
        self.__stop = True

    @property
    def stopped(self):
        return self.__stop
