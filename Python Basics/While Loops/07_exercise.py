width = int(input())
length = int(input())
height = int(input())
free_space = width * length * height

while True:
    command = input()
    if command == 'Done':
        print(f'{free_space} Cubic meters left.')
        break

    used_space = int(command)
    free_space -= used_space

    if free_space <= 0:
        print(f'No more free space! You need {abs(free_space)} Cubic meters more.')
        break
