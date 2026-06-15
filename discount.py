TAX_RATE = 0.13          # global constant (13% VAT)


def apply_discount(price, percent):
    """Returns price after applying discount percentage."""
    discount_amount = price * (percent / 100)
    return price - discount_amount


def apply_tax(price):
    """Returns price after adding TAX_RATE (13% VAT)."""
    return price * (1 + TAX_RATE)


def final_price(price, discount_pct):
    """Applies discount first, then adds tax."""
    discounted = apply_discount(price, discount_pct)
    return apply_tax(discounted)
