start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
combination = 0
magic_number_found = False

for current_number in range(start_interval, end_interval + 1):
    for second_number in range(start_interval, end_interval + 1):
        combination += 1

        if current_number + second_number == magic_number:
            print(f'Combination N:{combination} ({current_number} + {second_number} = {magic_number})')
            magic_number_found = True
            break
    if magic_number_found:
        break

else:
    print(f'{combination} combinations - neither equals {magic_number}')

