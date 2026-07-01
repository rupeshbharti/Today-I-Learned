def apply_discount(price, percent):
    """Returns discounted price based on a percentage"""
    return price * (1 - percent / 100)

def flat_discount(price):
    """Always subtracts 50 from price"""
    return price - 50
