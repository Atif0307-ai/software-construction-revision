from typing import TypedDict


class OrderItem(TypedDict):
    price: float
    qty: int

class Order(TypedDict):
    items: list[OrderItem]
    country: str
    member: bool



def calculate_sub_total(items : list[OrderItem]) -> float:
    total = 0.0

    for item in items:
        price = item["price"]
        quantity = item["qty"]

        if price <= 0 or quantity <= 0:
            continue

        total = total + price * quantity

    return total

def calculate_discount(total: float, is_member: bool) -> float:
    if not is_member:
        return 0.0
    if total > 100:
        return total * 0.2
    if total > 50:
        return total * 0.1

    return 0.0

def calculate_shipping_cost(country: str) -> float:

  if country == "PK":
    return 5.0

  if country == "US":
    return 15.0

  return 25.0

def calculate_order_total(order: Order) -> float:
    sub_total = calculate_sub_total(order["items"])
    discount_amount = calculate_discount(sub_total, order["member"])
    total = sub_total - discount_amount
    shipping_cost = calculate_shipping_cost(order["country"])

    total = total + shipping_cost
    
    return total