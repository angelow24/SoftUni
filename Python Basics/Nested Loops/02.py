first_num = int(input())
second_num = int(input())

for number in range(first_num, second_num + 1):
    number_to_str = str(number)
    even_numbers_sum = 0
    odd_numbers_sum = 0

    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            odd_numbers_sum += int(digit)
        else:
            even_numbers_sum += int(digit)

    if even_numbers_sum == odd_numbers_sum:
        print(number, end=' ')

