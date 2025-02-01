#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, title, price, quantity=1):
        for i in range(quantity):
            self.items.append(title)

        self.total += (price * quantity)
        self.previous_transactions.append(
            {"title":title, "price":price, "quantity":quantity}
        )

    def apply_discount(self):
        self.total *= 0.8
        if(self.total > 0):
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.") 

    def items(self):
        return self.items

    def void_last_transaction(self):
        if not self.previous_transactions:
            return
        self.total -= (
            self.previous_transactions[-1]['price'] *
                self.previous_transactions[-1]['quantity']
        )

        for _ in range(self.previous_transactions[-1]['quantity']):
            self.items.pop()

        self.previous_transactions.pop()








