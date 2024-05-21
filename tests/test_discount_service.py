#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
from dont_use_else.discount_service import DiscountService, DiscountType


def test_persentage_discount():
    discount_service = DiscountService()
    discount = discount_service.apply_discount(100, DiscountType.PERCENTAGE, 0.1)
    assert discount == 90


def test_wrong_persentage_discount():
    discount_service = DiscountService()
    try:
        discount_service.apply_discount(100, DiscountType.PERCENTAGE, 2)
    except ValueError as e:
        assert str(e) == "A percentage discount should be between 0.0 and 1.0"
    else:
        assert False


def test_absolute_discount():
    discount_service = DiscountService()
    discount = discount_service.apply_discount(100, DiscountType.ABSOLUTE, 10)
    assert discount == 90


def test_wrong_absolute_discount():
    discount_service = DiscountService()
    try:
        discount_service.apply_discount(100, DiscountType.ABSOLUTE, -10)
    except ValueError as e:
        assert str(e) == "An absolute discount should be positive"
    else:
        assert False


def test_no_discount():
    discount_service = DiscountService()
    discount = discount_service.apply_discount(100, DiscountType.NONE, 0)
    assert discount == 100


def test_none_discount():
    discount_service = DiscountService()
    discount = discount_service.apply_discount(100, None, 0)
    assert discount == 100
