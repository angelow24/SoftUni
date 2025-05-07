player_name = input()

successful_shots = 0
unsuccessful_shots = 0
starting_points = 301

command = input()
while command != 'Retire':
    zone = str(command)
    if starting_points > 0:
        shot_points = int(input())

        if zone == 'Double':
            shot_points *= 2
        elif zone == 'Triple':
            shot_points *= 3

        if shot_points > starting_points:
            unsuccessful_shots += 1
            command = input()
            continue
        elif shot_points <= starting_points:
            starting_points -= shot_points
            successful_shots += 1
            if starting_points == 0:
                print(f'{player_name} won the leg with {successful_shots} shots.')
                break
            command = input()

if command == 'Retire':
    print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')
