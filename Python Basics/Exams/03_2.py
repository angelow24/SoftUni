# Етап на първенството – текст - “Quarter final ”, “Semi final” или “Final”
tournament_stage = input()
# Вид на билета – текст - “Standard”, “Premium” или “VIP”
ticket_type = input()
# Брой билети – цяло число в интервала [1 … 30]
ticket_count = int(input())
# Снимка с трофея – символ – 'Y' (да) или 'N' (не)
photo_with_trophy = input()

ticket_price = 0
photo_with_trophy_cost = 0

if photo_with_trophy == 'Y':
    photo_with_trophy_cost += 40 * ticket_count

if tournament_stage == 'Quarter final':
    if ticket_type == 'Standard':
        ticket_price = 55.50
    elif ticket_type == 'Premium':
        ticket_price = 105.20
    elif ticket_type == 'VIP':
        ticket_price = 118.90

elif tournament_stage == 'Semi final':
    if ticket_type == 'Standard':
        ticket_price = 75.88
    elif ticket_type == 'Premium':
        ticket_price = 125.22
    elif ticket_type == 'VIP':
        ticket_price = 300.40

elif tournament_stage == 'Final':
    if ticket_type == 'Standard':
        ticket_price = 110.10
    elif ticket_type == 'Premium':
        ticket_price = 160.66
    elif ticket_type == 'VIP':
        ticket_price = 400

total_cost = ticket_price * ticket_count

if total_cost > 4000:
    if photo_with_trophy == 'Y':
        photo_with_trophy_cost = 0
    total_cost -= (total_cost * 0.25)
elif total_cost > 2500:
    total_cost -= (total_cost * 0.10)

grand_total = total_cost + photo_with_trophy_cost

print(f'{grand_total:.2f}')





