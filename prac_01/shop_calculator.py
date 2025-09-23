"""
CP1404 Practical
This program is for a shop to calculate the total price of all the items a customer buys.
If the purchase is above $100 a discount of 10% will be applied
"""
DISCOUNT = 0.9
total_price = 0

number_of_items = int(input("Number of items? "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items? "))

for i in range(1, number_of_items+1):
    price_of_item = float(input("Price of item? "))
    total_price += price_of_item

discount_price = total_price * DISCOUNT
print(f"Total price for {number_of_items} items is ${discount_price:.2f}")