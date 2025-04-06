command = input()
non_prime_numbers = 0
prime_numbers = 0

while command != 'stop':
    number = int(command)

    if number < 0:
        print(f'Number is negative.')
        command = input()
        continue

    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers += number
    else:
        non_prime_numbers += number

    command = input()

print(f'Sum of all prime numbers is: {prime_numbers}')
print(f'Sum of all non prime numbers is: {non_prime_numbers}')

