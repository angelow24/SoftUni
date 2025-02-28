budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

price_video_cards = video_cards * 250
price_processors = processors * (price_video_cards * 0.35)
price_ram = ram * (price_video_cards * 0.10)

total_cost_for_equipment = price_processors + price_ram + price_video_cards

if video_cards > processors:
    total_cost_for_equipment -= (total_cost_for_equipment * 0.15)

if budget >= total_cost_for_equipment:
    print(f'You have {budget - total_cost_for_equipment:.2f} leva left!')
else:
    print(f'Not enough money! You need {total_cost_for_equipment - budget:.2f} leva more!')