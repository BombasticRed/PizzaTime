from pizzapi import *
def OrderPizza(FName, LName, Email, PhoneNumber, add, City, State, Zip, CardN, CVV, Exp, CardZip, FoodItem):
   print(add)
   print(City)
   print(State)
   print(CardN)
   print(CVV)
   print(Exp)
   print(CardZip)
   customer = Customer(FName, LName, Email, PhoneNumber)
   address = Address(add, City, State, Zip)
   store = address.closest_store()
   order = Order(store, customer, address)
   order.add_item(FoodItem)
   card = PaymentObject(CardN, Exp, CVV, CardZip)
   order.place(card)
   #######