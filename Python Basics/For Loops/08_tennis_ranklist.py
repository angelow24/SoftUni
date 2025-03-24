from math import floor

tournaments_participated = int(input())
starting_points = int(input())

points_earned = 0
wins = 0

for _ in range(tournaments_participated):
    ranking = input()
    if ranking == 'W':
        points_earned += 2000
        wins += 1
    elif ranking == 'F':
        points_earned += 1200
    elif ranking == 'SF':
        points_earned += 720

end_season_points = starting_points + points_earned
average_earned_points = points_earned / tournaments_participated
wins_percentage = (wins / tournaments_participated) * 100

print(f'Final points: {end_season_points}')
print(f'Average points: {floor(average_earned_points)}')
print(f'{wins_percentage:.2f}%')


