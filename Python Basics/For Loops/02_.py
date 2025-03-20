number = int(input())

max_number = 0
total_sum = 0

for _ in range(number):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    total_sum += current_number

difference = total_sum - max_number
difference_without_max_number = max_number - difference

if difference == max_number:
    print('Yes')
    print(f'Sum = {difference}')
else:
    print('No')
    print(f'Diff = {abs(difference_without_max_number)}')