from decimal import Decimal
from typing import Protocol


class Discount(Protocol):
    def apply(self, amount: float) -> float:
        pass


class NoDiscount:
    @staticmethod
    def apply(amount: float) -> float:
        return amount


class AbsoluteDiscount:
    def __init__(self, discount: float):
        self.discount: float = discount

    def apply(self, amount: float) -> float:
        if self.discount < Decimal(0):
            raise ValueError("An absolute discount should be positive")
        reduce_amount: float = amount - self.discount
        return reduce_amount


class PercentageDiscount:
    def __init__(self, discount: float):
        self.discount: float = discount

    def apply(self, amount: float) -> float:
        if self.discount < Decimal(0) or self.discount > Decimal(1):
            raise ValueError("A percentage discount should be between 0.0 and 1.0")
        reduce_amount: float = amount - amount * self.discount
        return reduce_amount


class DiscountService:
    @staticmethod
    def apply_discount(amount: float, discount: Discount) -> float:
        discount = NoDiscount() if discount is None else discount

        return discount.apply(amount)
