n = int(input())

sum_left_side = 0
sum_right_side = 0

for _ in range(n):
    left_side_number = int(input())
    sum_left_side += left_side_number
for _ in range(n):
    right_side_number = int(input())
    sum_right_side += right_side_number

if sum_left_side == sum_right_side:
    print(f'Yes, sum = {sum_left_side}')
else:
    print(f'No, diff = {abs(sum_left_side - sum_right_side)}')
