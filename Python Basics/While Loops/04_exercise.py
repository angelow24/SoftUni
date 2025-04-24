steps_achieved = 0

while True:
    command = input()
    if command == 'Going home':
        steps_going_home = int(input())
        steps_achieved += steps_going_home
        break

    steps = int(command)
    steps_achieved += steps

    if steps_achieved > 10000:
        break

diff = steps_achieved - 10000
is_goal_achieved = steps_achieved >= 10000
if not is_goal_achieved:
    print(f'{abs(diff)} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
