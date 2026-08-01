prices = {
    "яблоко": 50,
    "банан": 40,
    "апельсин": 20,
}

cart = {
    "яблоко": 3,
    "банан": 2,
    "апельсин": 1,
}


def total(cart, prices):
    return sum(prices[fruit] * quantity for fruit, quantity in cart.items())
