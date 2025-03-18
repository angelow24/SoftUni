n = int(input())

odd_numbers = 0
even_numbers = 0

for index in range(n):
    current_number = int(input())
    if index % 2 == 0:
        even_numbers += current_number
    else:
        odd_numbers += current_number

if odd_numbers == even_numbers:
    print(f'Yes')
    print(f'Sum = {odd_numbers}')
else:
    print(f'No')
    print(f'Diff = {abs(odd_numbers - even_numbers)}')