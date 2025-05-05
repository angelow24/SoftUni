game_1 = input()
game_2 = input()
game_3 = input()

wins = 0
loses = 0
draws = 0

first_digit = int(game_1[0])
third_digit = int(game_1[2])
if first_digit > third_digit:
    wins += 1
elif first_digit == third_digit:
    draws += 1
else:
    loses += 1

first_digit2 = int(game_2[0])
third_digit2 = int(game_2[2])
if first_digit2 > third_digit2:
    wins += 1
elif first_digit2 == third_digit2:
    draws += 1
else:
    loses += 1

first_digit3 = int(game_3[0])
third_digit3 = int(game_3[2])
if first_digit3 > third_digit3:
    wins += 1
elif first_digit3 == third_digit3:
    draws += 1
else:
    loses += 1

print(f'Team won {wins} games.')
print(f'Team lost {loses} games.')
print(f'Drawn games: {draws}')