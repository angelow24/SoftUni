# В зависимост от сезона:
# · Цената за наем на кораба през пролетта е 3000 лв.;
# · Цената за наем на кораба през лятото и есента е 4200 лв.;
# · Цената за наем на кораба през зимата е 2600 лв.

# В зависимост от броя на групата има различна отстъпка:
# · Ако групата е от 7 до 11 човека включително - отстъпка от 15%;
# · Ако групата е от 12 нагоре - отстъпка от 25%.

# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен - тогава нямат допълнителна отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
budget = int(input())
season = input()  # Spring", "Summer", "Autumn" or "Winter"
fisherman = int(input())

price_boat = 0
discount = 0

if season == 'Spring':
    price_boat = 3000
    if fisherman <= 6:
        discount = 0.10
    elif 7 <= fisherman <= 11:
        discount = 0.15
    elif fisherman >= 12:
        discount = 0.25
elif season == 'Summer' or season == 'Autumn':
    price_boat = 4200
    if fisherman <= 6:
        discount = 0.10
    elif 7 <= fisherman <= 11:
        discount = 0.15
    elif fisherman >= 12:
        discount = 0.25
elif season == 'Winter':
    price_boat = 2600
    if fisherman <= 6:
        discount = 0.10
    elif 7 <= fisherman <= 11:
        discount = 0.15
    elif fisherman >= 12:
        discount = 0.25

price_after_discount = price_boat * (1 - discount)
additional_discount = 0

if fisherman % 2 == 0 and not season == 'Autumn':
    additional_discount = 0.05

price_after_discount = price_after_discount * (1 - additional_discount)

if budget >= price_after_discount:
    print(f'Yes! You have {budget - price_after_discount:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(budget - price_after_discount):.2f} leva.')
