import random
import threading
import time

ALLOWED_PRODUCTS = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


class Customer:
    def __init__(self, name, product):
        self.name = name
        self.product_of_interest = product

    def notify(self, product_name):
        print(
            f"[NOTIFICATION] {self.name} has been notified that the {product_name} is now available."
        )


class Store:
    def __init__(self):
        self.customers = set()
        self.products = ["A", "B", "C"]

    def register_customer(self, customer):
        self.customers.add(customer)

    def get_customers(self):
        return self.customers[:]

    def receive_product(self, product_name):
        self.products.append(product_name)
        for customer in self.customers:
            customer.notify(product_name)

    def has_product(self, product_name):
        return product_name in self.products


class Product:
    pass


class StoppableThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


def customer_thread(customer: Customer, store: Store):
    print(
        f"[START] {customer.name} is looking for the {customer.product_of_interest} in the store."
    )
    while not thread.stopped():
        time.sleep(
            random.random() * 5
        )  # wait for a random amount of time between 0 and 5 seconds
        if store.has_product(customer.product_of_interest):
            print(
                f"[YES] {customer.name} found the {customer.product_of_interest} in the store."
            )
            break
        print(
            f"[NO NOT AGAIN] {customer.name} did NOT find the {customer.product_of_interest} in the store."
        )


def product_thread(store: Store):
    while not thread.stopped():
        time.sleep(3)  # wait for a random amount of time between 0 and 5 seconds
        random_choice = random.choice(ALLOWED_PRODUCTS)
        print(f"[STORE] New product {random_choice} has arrived.")
        store.receive_product(random_choice)


if __name__ == "__main__":
    store = Store()
    alice = Customer("Alice", random.choice(ALLOWED_PRODUCTS))
    bob = Customer("Bob", random.choice(ALLOWED_PRODUCTS))
    charlie = Customer("Charlie", random.choice(ALLOWED_PRODUCTS))
    david = Customer("David", random.choice(ALLOWED_PRODUCTS))
    eve = Customer("Eve", random.choice(ALLOWED_PRODUCTS))
    frank = Customer("Frank", random.choice(ALLOWED_PRODUCTS))

    threads = []
    for customer in [alice, bob, charlie, david, eve, frank]:
        store.register_customer(customer)
        thread = StoppableThread(
            target=customer_thread, args=(customer, product, store)
        )
        threads.append(thread)

    product_thread = StoppableThread(target=product_thread, args=(store,))
    threads.append(product_thread)

    for thread in threads:
        thread.start()

    while True:
        print()
        print("1. Register as a customer")
        print("2. Notify of new product arrival")
        print("3. Exit")
        print()
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter your name: ")
            customer = Customer(name, random.choice(ALLOWED_PRODUCTS))
            store.register_customer(customer)
            print(f"Customer {name}  has visited the store.")
        elif choice == "2":
            product_name = input("Enter the name of the new product: ")
            store.receive_product(product_name)
        elif choice == "3":
            for thread in threads:
                thread.stop()
            break
        else:
            print("Invalid option. Please choose again.")
