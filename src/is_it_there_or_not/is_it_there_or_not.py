from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, store: "Store"):
        pass


class Product:
    def __init__(self, name: str):
        self.name: str = name

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name


class Store:
    def __init__(self):
        self.observers: set[Observer] = set()
        self.stock: list[Product] = []

    def add_observer(self, observer: Observer):
        self.observers.add(observer)

    def remove_observer(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers.copy():
            observer.update(self)

    def delivery(self, product: Product):
        self.stock.append(product)
        self.notify_observers()

    def has_product(self, product: Product) -> [Product | None]:
        return product in self.stock


class Customer(Observer):
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
            store.add_observer(self)
            return False
        self.happy = True
        return True

    def update(self, store: Store):
        print(f"{self.name} is going shopping!")
        if self.go_shopping(store):
            store.remove_observer(self)

    @property
    def is_happy(self):
        return self.happy
