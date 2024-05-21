from decimal import Decimal
from enum import Enum, auto


class DiscountType(Enum):
    NONE = auto()
    PERCENTAGE = auto()
    ABSOLUTE = auto()


class DiscountService:
    @staticmethod
    def apply_discount(amount, discount_type, discount):
        discount_type = DiscountType.NONE if discount_type is None else discount_type

        if discount_type == DiscountType.PERCENTAGE:
            if discount < Decimal(0) or discount > Decimal(1):
                raise ValueError("A percentage discount should be between 0.0 and 1.0")
            reduce_amount = amount - amount * discount
        elif discount_type == DiscountType.ABSOLUTE:
            if discount < Decimal(0):
                raise ValueError("An absolute discount should be positive")
            reduce_amount = amount - discount
        else:
            reduce_amount = amount

        return reduce_amount
