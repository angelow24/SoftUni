record_in_seconds = float(input())
distance_in_meters_to_swim = float(input())
time_to_swim_one_meter_in_seconds = float(input())

delay = (distance_in_meters_to_swim // 15) * 12.5
world_record_attempt = (distance_in_meters_to_swim * time_to_swim_one_meter_in_seconds) + delay

if world_record_attempt < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {world_record_attempt:.2f} seconds.')
else:
    print(f'No, he failed! He was {abs(world_record_attempt - record_in_seconds):.2f} seconds slower.')
