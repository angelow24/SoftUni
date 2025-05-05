minutes_controla = int(input())
seconds_controla = int(input())
chute_length = float(input())
seconds_for_100_meters = int(input())

minutes_controla_to_seconds = minutes_controla * 60
total_time_controla = minutes_controla_to_seconds + seconds_controla # 80

delay = chute_length / 120
delay_in_sec = delay * 2.5

marin_performance = (chute_length / 100) * seconds_for_100_meters - delay_in_sec
diff = total_time_controla - marin_performance

if marin_performance > total_time_controla:
    print(f'No, Marin failed! He was {abs(diff):.3f} second slower.')
else:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {marin_performance:.3f}.')