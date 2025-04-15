total_money = 0

while True:
    data = input()

    if data == 'NoMoreMoney':
        break

    current_sum = float(data)

    if current_sum >= 0:
        total_money += current_sum
        print(f'Increase: {current_sum:.2f}')
    else:
        print(f'Invalid operation!')
        break
print(f'Total: {total_money:.2f}')