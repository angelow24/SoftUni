money_needed_trip = float(input())
available_money = float(input())
consecutive_days_spend = 0
is_money_saved = False
days = 0

while True:
    command = input()
    current_sum = float(input())
    days += 1

    if command == 'spend':
        available_money -= current_sum
        consecutive_days_spend += 1
        if available_money < 0:
            available_money = 0
        if consecutive_days_spend == 5:
            is_money_saved = False
            break
    if command == 'save':
        available_money += current_sum
        consecutive_days_spend = 0
    if available_money >= money_needed_trip:
        is_money_saved = True
        break

if is_money_saved:
    print(f'You saved the money for {days} days.')
else:
    print(f"You can't save the money.")
    print(days)

