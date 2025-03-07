budget = float(input())
season = input()  # summer or winter

destination = ''
vacation_type = ''
money_spent = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacation_type = 'Camp'
        money_spent = budget * 0.30
    elif season == 'winter':
        vacation_type = 'Hotel'
        money_spent = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    vacation_type = 'Camp'
    if season == 'summer':
        money_spent = budget * 0.40
    elif season == 'winter':
        vacation_type = 'Hotel'
        money_spent = budget * 0.80
elif budget > 1000:
    destination = 'Europe'
    vacation_type = 'Hotel'
    money_spent = budget * 0.90

print(f'Somewhere in {destination}')
print(f'{vacation_type} - {money_spent:.2f}')

