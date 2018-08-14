number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print('Invalid number of items!')
    number_of_items = int(input("Number of items: "))

total_item_price = 0
for i in range(1, number_of_items + 1):
    item_price = float(input("Price of item: "))
    total_item_price += item_price
discount = 0.9
if total_item_price > 100:
    total_item_price = total_item_price * discount
print('Total price for', number_of_items, 'items is $ {:.2f}'.format(total_item_price))
