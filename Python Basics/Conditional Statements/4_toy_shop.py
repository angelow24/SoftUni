price_needed_for_trip = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_teddy_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

total_number_ordered = number_puzzles + number_dolls + number_teddy_bears + number_minions + number_trucks
total_price = ((number_puzzles * 2.6)
              + (number_dolls * 3)
              + (number_teddy_bears * 4.1)
              + (number_minions * 8.2)
              + (number_trucks * 2))

if total_number_ordered >= 50:
    total_price -= (total_price * 0.25)

total_price -= (total_price * 0.10)

if total_price >= price_needed_for_trip:
    print(f'Yes! {total_price - price_needed_for_trip:.2f} lv left.')
else:
    print(f'Not enough money! {price_needed_for_trip - total_price:.2f} lv needed.')
