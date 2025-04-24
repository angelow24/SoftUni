height = int(input())
width = int(input())
cake_pieces = height * width

while True:
    command = input()

    if command == 'STOP':
        print(f'{cake_pieces} pieces are left.')
        break

    pieces_eaten = int(command)
    cake_pieces -= pieces_eaten

    if cake_pieces <= 0:
        print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
        break
