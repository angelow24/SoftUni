flag = False
while True:
    destination = input()
    if destination == 'End':
        flag = True
        break
    budget_needed = float(input())
    money_saved = 0
    while destination != 'End':
        current_savings = float(input())
        money_saved += current_savings
        if money_saved >= budget_needed:
            print(f'Going to {destination}!')
            break

