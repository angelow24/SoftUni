lilly_age = int(input())
washing_machine = float(input())
toy_price = int(input())

saved_money = 0
money_gift = 10
toys_number = 0

for i in range(1, lilly_age + 1):
    if i % 2 == 0:
        saved_money += money_gift
        money_gift += 10
        saved_money -= 1
    else:
        toys_number += 1

toys_money = toys_number * toy_price
total_money_saved = toys_money + saved_money
money_after_purchase = total_money_saved - washing_machine

if total_money_saved >= washing_machine:
    print(f'Yes! {money_after_purchase:.2f}')
else:
    print(f'No! {abs(money_after_purchase):.2f}')
