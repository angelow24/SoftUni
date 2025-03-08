# "room for one person" – 18.00 лв за нощувка
# "apartment" – 25.00 лв за нощувка
# "president apartment" – 35.00 лв за нощувка

days = int(input())
property_type = input() # "room for one person", "apartment" или "president apartment
satisfaction = input()

nights_to_stay = days - 1
discount = 0
price_per_night = 0
additional_discount = 0


if days < 10:
    if property_type == 'room for one person':
        price_per_night = 18.00
    elif property_type == 'apartment':
        price_per_night = 25.00 * (1 - 0.30)
    elif property_type == 'president apartment':
        price_per_night = 35.00 * (1 - 0.10)
elif 10 < days <= 15:
    if property_type == 'room for one person':
        price_per_night = 18.00
    elif property_type == 'apartment':
        price_per_night = 25.00 * (1 - 0.35)
    elif property_type == 'president apartment':
        price_per_night = 35.00 * (1 - 0.15)
elif days > 15:
    if property_type == 'room for one person':
        price_per_night = 18.00
    elif property_type == 'apartment':
        price_per_night = 25.00 * (1 - 0.50)
    elif property_type == 'president apartment':
        price_per_night = 35.00 * (1 - 0.20)

if satisfaction == 'positive':
    total_cost = (price_per_night * nights_to_stay) * 1.25
elif satisfaction == 'negative':
    total_cost = (price_per_night * nights_to_stay) * (1 - 0.10)

print(f'{total_cost:.2f}')


