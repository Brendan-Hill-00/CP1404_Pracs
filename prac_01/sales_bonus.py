sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus_rate = 0.1
        bonus = sales * bonus_rate
    else:
        bonus_rate = 0.15
        bonus = sales * bonus_rate
print('Bonus Earned: $' + str(bonus))
sales = float(input("Enter sales: $"))
