hours = int(input())
minutes = int(input()) + 15


if minutes >= 60:
    hours += 1
    minutes -= 60
if hours >= 24:
    hours -= 24

if minutes <= 10:
    print(f"{hours}:{minutes:02d}")
else:
    print(f'{hours}:{minutes}')
