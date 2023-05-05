from collections import namedtuple
from dataclasses import dataclass


@dataclass
class Product:
    base_price: float
    discount_threshold: float
    discount_rate: float


@dataclass
class ShippingType:
    discount_threshold: float
    discounted_fee: float
    fee_per_case: float


PriceData = namedtuple('PriceData', 'base_price quantity discount')


def calculate_pricing_data(
        product: Product,
        quantity: int
) -> PriceData:
    """Phase 1"""
    base_price = product.base_price * quantity
    discount = (max(quantity - product.discount_threshold, 0)
                * product.base_price * product.discount_rate)
    return PriceData(base_price, quantity, discount)


def apply_shipping(
        price_data: PriceData,
        shipping_type: ShippingType,
) -> float:
    shipping_per_case = (
        shipping_type.discounted_fee
        if price_data.base_price > shipping_type.discount_threshold
        else shipping_type.fee_per_case
    )
    shipping_cost = price_data.quantity * shipping_per_case
    return price_data.base_price - price_data.discount + shipping_cost


def get_price_order(
        product: Product,
        quantity: int,
        shipping_type: ShippingType
) -> float:
    # Phase 2
    return apply_shipping(
        calculate_pricing_data(product, quantity),
        shipping_type
    )
