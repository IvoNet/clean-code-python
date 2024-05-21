from decimal import Decimal
from enum import Enum, auto
from typing import Protocol


class DiscountType(Enum):
    NONE = auto()
    PERCENTAGE = auto()
    ABSOLUTE = auto()


# create a Prototype of the Discount class with an apply method
class Discount(Protocol):
    def apply(self, amount: Decimal) -> Decimal:
        pass


class NoDiscount:
    @staticmethod
    def apply(amount):
        return amount


class AbsoluteDiscount:
    def __init__(self, discount):
        self.discount = discount

    def apply(self, amount):
        if self.discount < Decimal(0):
            raise ValueError("An absolute discount should be positive")
        reduce_amount = amount - self.discount
        return reduce_amount


class PercentageDiscount:
    def __init__(self, discount):
        self.discount = discount

    def apply(self, amount):
        if self.discount < Decimal(0) or self.discount > Decimal(1):
            raise ValueError("A percentage discount should be between 0.0 and 1.0")
        reduce_amount = amount - amount * self.discount
        return reduce_amount


class DiscountService:
    @staticmethod
    def apply_discount(amount, discount: Discount):
        discount = NoDiscount() if discount is None else discount

        return discount.apply(amount)
