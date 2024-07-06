import random


def get_numbers_ticket(min, max, quantity):
    if min < 1:
        print("Wrong min")
        return []
    if max > 1000 or max <= min:
        print("Wrong max")
        return []

    maxQuantity = max - min
    if quantity < 1 or quantity > maxQuantity:
        print("Wrong quantity")
        return []

    return sorted(random.sample(range(min, max), quantity))
