#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.lastItem = None

  def add_item(self, title, price, quantity = 1):
    for i in range(0, quantity):
      self.items.append(title)
    self.total += price * quantity
    self.lastItem = (title, price, quantity)
  
  def apply_discount(self):
    self.total *= (100-self.discount)/100
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      formatted_total = "${:,.2f}".format(self.total).rstrip('0').rstrip('.')
      print("After the discount, the total comes to {}.".format(formatted_total))

  def void_last_transaction(self):
    self.total -= self.lastItem[1] * self.lastItem[2]
    for i in range(0, self.lastItem[2]):
      self.items.remove(self.lastItem[0])