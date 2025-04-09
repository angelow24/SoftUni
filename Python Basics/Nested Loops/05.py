number_input = int(input())

for number in range(1111, 10000):

    number_as_str = str(number)

    is_magic_number = True
    for digit in number_as_str:
        digit_as_int = int(digit)

        if digit_as_int == 0:
            is_magic_number = False
            break

        if number_input % digit_as_int != 0:
            is_magic_number = False
            break

    if is_magic_number:
        print(number, end=' ')
