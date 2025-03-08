exam_time_hour = int(input())
exam_time_minutes = int(input())
arrival_time_hours = int(input())
arrival_time_minutes = int(input())

when_arrived = ''

time_arrived = (arrival_time_hours * 60) + arrival_time_minutes
time_exam = (exam_time_hour * 60) + exam_time_minutes
time_difference = time_exam - time_arrived

hours = abs(time_difference) // 60
minutes = abs(time_difference) % 60

if time_difference < 0:
    when_arrived = 'Late'
    if time_difference >= -59:
        print(f'{when_arrived}')
        print(f'{abs(time_difference)} minutes after the start')
    else:
        print(f'{when_arrived}')
        print(f'{hours}:{minutes:02d} hours after the start')
elif 31 <= time_difference <= 59:
    when_arrived = 'Early'
    print(f'{when_arrived}')
    print(f'{abs(time_difference):02d} minutes before the start')
elif time_difference > 59:
    when_arrived = 'Early'
    print(f'{when_arrived}')
    print(f'{time_difference // 60}:{(time_difference % 60):02d} hours before the start')
elif time_difference == 0:
    when_arrived = 'On time'
    print(when_arrived)
elif time_difference <= 30:
    when_arrived = 'On time'
    print(f'{when_arrived}')
    print(f'{abs(time_difference)} minutes before the start')



