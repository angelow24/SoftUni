# · Premiere - премиерна прожекция, на цена 12.00 лева;
# · Normal - стандартна прожекция, на цена 7.50 лева;
# · Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.

type_projection = input()
rows = int(input())
cols = int(input())

total_capacity = rows * cols
price_for_tickets = 0

if type_projection == 'Premiere':
    price_for_tickets = 12.00
elif type_projection == 'Normal':
    price_for_tickets = 7.50
elif type_projection == 'Discount':
    price_for_tickets = 5.00

revenue = total_capacity * price_for_tickets

print(f'{revenue:.2f} leva')
