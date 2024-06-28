class Product:
    def __init__(self, name: str):
        self.name: str = name

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name


class Store:
    def __init__(self):
        self.stock: list[Product] = []

    def delivery(self, product: Product):
        self.stock.append(product)

    def has_product(self, product: Product):
        return product in self.stock


class Customer:
    def __init__(self, name: str, product: Product):
        self.name: str = name
        self.product_of_interest = product

    def go_shopping(self, store: Store) -> bool:
        """
        Checks if the customer can purchase their desired product.

        Args:
            store (Store): The store where the product is to be purchased.

        Returns:
            bool: True if the product is available in the store, False otherwise.
        """
        return store.has_product(self.product_of_interest)
