n1 = int(input())
n2 = int(input())
operation = input()

even_or_odd = ''
result = 0

if operation == '+':
    result = n1 + n2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{n1} + {n2} = {result} - {even_or_odd}')
elif operation == '-':
    result = n1 - n2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{n1} - {n2} = {result} - {even_or_odd}')
elif operation == '*':
    result = n1 * n2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{n1} * {n2} = {result} - {even_or_odd}')
elif operation == '/':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = (n1 / n2)
        print(f'{n1} / {n2} = {result:.2f}')
elif operation == '%':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = (n1 % n2)
        print(f'{n1} % {n2} = {result}')
