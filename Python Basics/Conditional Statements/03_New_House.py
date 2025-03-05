# · Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# · Ако Нели купи повече от 90 Далии - 15% отстъпка от крайната цена;
# · Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# · Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# · Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

type_flower = input()  # Roses", "Dahlias", "Tulips", "Narcissus" or "Gladiolus
number_of_flowers = int(input())
budget = int(input())

discount = 0
total_price = 0
price_of_flower = 0

if type_flower == 'Roses':
    price_of_flower = 5
    if number_of_flowers > 80:
        discount = 0.10
elif type_flower == 'Dahlias':
    price_of_flower = 3.80
    if number_of_flowers > 90:
        discount = 0.15
elif type_flower == 'Tulips':
    price_of_flower = 2.80
    if number_of_flowers > 80:
        discount = 0.15
elif type_flower == 'Narcissus':
    price_of_flower = 3
    if number_of_flowers < 120:
        discount = -0.15
elif type_flower == 'Gladiolus':
    price_of_flower = 2.50
    if number_of_flowers < 80:
        discount = -0.20

total_price = (price_of_flower * number_of_flowers) * (1 - discount)
money_left = budget - total_price

if budget >= total_price:
    print(f'Hey, you have a great garden with {number_of_flowers} {type_flower} and {money_left:.2f} leva left.')
elif budget < total_price:
    print(f'Not enough money, you need {abs(money_left):.2f} leva more.')


# Да се отпечата на конзолата на един ред:
# · Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# · Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.