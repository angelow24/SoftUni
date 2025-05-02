money_needed = int(input())
day = 0
paid_by_card = 0
card_counter = 0
paid_by_cash = 0
cash_counter = 0

while True:
    command = input()

    if command == 'End':
        print(f'Failed to collect required money for charity.')
        break

    money_earned = int(command)
    day += 1

    if day % 2 == 0:
        if money_earned <= 10:
            print('Error in transaction!')
        else:
            paid_by_card += money_earned
            card_counter += 1
            print(f'Product sold! ')
    else:
        if money_earned >= 100:
            print('Error in transaction!')
        else:
            paid_by_cash += money_earned
            cash_counter += 1
            print(f'Product sold! ')
    if money_needed - (paid_by_cash + paid_by_card) <= 0:
        average_cash = paid_by_cash / cash_counter
        average_card = paid_by_card / card_counter
        print(f"Average CS: {average_cash:.2f}")
        print(f"Average CC: {average_card:.2f}")
        break
