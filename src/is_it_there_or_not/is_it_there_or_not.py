class Product:
    def __init__(self, name: str):
        self.name: str = name

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name


class Customer:
    def __init__(self, name: str, product: Product):
        self.name: str = name
        self.product_of_interest = product


class Store:
    def __init__(self):
        self.stock: list[Product] = []

    def receive_product(self, product: Product):
        self.stock.append(product)

    def has_product(self, product: Product):
        return product in self.stock
