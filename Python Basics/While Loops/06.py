import sys

max_number = -sys.maxsize

while True:
    data = input()
    if data == 'Stop':
        print(max_number)
        break

    number = int(data)

    if max_number <= number:
        max_number = number


