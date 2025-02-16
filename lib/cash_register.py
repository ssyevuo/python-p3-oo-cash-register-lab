#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = 0

  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    self.items.extend([title] * quantity)
    self.last_transaction = price * quantity
    return self.total
  
  def apply_discount(self):
    if self.discount > 0:
      self.total -= self.total * (self.discount / 100)
      int_total = int(self.total) if self.total.is_integer() else round(self.total, 2)
      print(f"After the discount, the total comes to ${int_total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_transaction
    self.last_transaction = 0


