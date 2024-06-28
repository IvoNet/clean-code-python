class Product:
    def __init__(self, name):
        self.name = name


class Customer:
    def __init__(self, name, product: Product):
        self.name = name
        self.product_of_interest = product


class Store:
    def __init__(self, product: Product):
        self.products: list[Product] = [
            product,
        ]

    def receive_product(self, product: Product):
        self.products.append(product)

    def has_product(self, product: Product):
        return product in self.products


PRODUCTS = {
    "coffee": Product("Coffee"),
    "tea": Product("tea"),
    "milk": Product("milk"),
    "sugar": Product("sugar"),
    "bread": Product("bread"),
    "butter": Product("butter"),
    "jam": Product("jam"),
    "honey": Product("honey"),
    "iphone": Product("iPhone"),
    "samsung": Product("Samsung"),
    "nokia": Product("Nokia"),
    "sony": Product("Sony"),
}
