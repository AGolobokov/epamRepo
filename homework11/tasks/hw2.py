"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""


class Order:

    morning_discount = 0.25

    def __init__(self, price, discount=None):
        self.price = price
        self.discount = discount

    def final_price(self):
        if self.discount:
            return self.price - self.discount(self)
        return self.price - self.price * self.morning_discount


def discount_on_the_morning(order):

    return order.price * 0.5


def discounts_for_the_elderly(order):

    return order.price * 0.9


if __name__ == "__main__":

    order_1 = Order(100, discount_on_the_morning)
    assert order_1.final_price() == 50

    order_2 = Order(100, discounts_for_the_elderly)
    assert order_2.final_price() == 10
