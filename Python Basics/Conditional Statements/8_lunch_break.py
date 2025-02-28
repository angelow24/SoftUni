from math import ceil

series_name = input()
time_for_one_episode = int(input())
free_time = int(input())

lunch_time = free_time / 8
relax_time = free_time / 4
time_left_for_watching = free_time - (lunch_time + relax_time + time_for_one_episode)

if time_left_for_watching >= 0:
    print(f'You have enough time to watch {series_name} and left with {ceil(time_left_for_watching)}'
          f' minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need "
          f"{ceil(abs(time_left_for_watching))} more minutes.")
