budget = float(input())
number_statists = int(input())
price_for_costume = float(input())

decor_price = budget * 0.10
clothes_price = price_for_costume * number_statists

if number_statists > 150:
    clothes_price -= (clothes_price * 0.10)

money_needed = clothes_price + decor_price

if money_needed > budget:
    print('Not enough money!')
    print(f'Wingard needs {money_needed - budget:.2f} leva more.')
else:
    print("Action!")
    print(f'Wingard starts filming with {budget - money_needed:.2f} leva left.')