class Customer:
    def __init__(self, name, product):
        self.name = name
        self.product_of_interest = product


class Store:
    def __init__(self, product):
        self.customers = set()
        self.products = [
            product,
        ]

    def receive_product(self, product_name):
        self.products.append(product_name)

    def has_product(self, product_name):
        return product_name in self.products


class Product:
    pass
