from abc import ABC, abstractmethod


class Observer(ABC):
    """The Observer interface declares the update method, used by subjects."""

    @abstractmethod
    def update(self, store: "Store") -> None:
        pass


class Subject(ABC):
    """The Subject interface declares a set of methods for managing subscribers."""

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Product:
    def __init__(self, name: str):
        self.name: str = name

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name


class Store(Subject):
    def __init__(self):
        self.observers: set[Observer] = set()
        self.stock: list[Product] = []

    def attach(self, observer: Observer) -> None:
        self.observers.add(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self) -> None:
        for observer in self.observers.copy():
            observer.update(self)

    def delivery(self, product: Product) -> None:
        self.stock.append(product)
        self.notify()

    def has_product(self, product: Product) -> bool:
        return product in self.stock


class Customer(Observer):  # ConcreteObserver
    def __init__(self, name: str, product: Product):
        self.name: str = name
        self.product_of_interest = product
        self.happy: bool = False

    def go_shopping(self, store: Store) -> bool:
        """
        Checks if the customer can purchase their desired product.

        Args:
            store (Store): The store where the product is to be purchased.

        Returns:
            bool: True if the product is available in the store, False otherwise.
        """
        if not store.has_product(self.product_of_interest):
            store.attach(self)
            return False
        self.happy = True
        return True

    def update(self, store: Store):
        """Now we will only go shopping when we get a notification from the store.
        It does not necessarily mean that the product I am looking for is available, only that the store has changed.
        You might even want to specialize the observer pattern to only notify when the
        product I am looking for is available. But that is an exercise for you and you may notify
        me when you did that :-)."""
        print(f"{self.name} is going shopping!")
        if self.go_shopping(store):
            store.detach(self)

    @property
    def is_happy(self):
        return self.happy
