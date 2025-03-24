groups_participants = int(input())

musala = 0
montblanc = 0
kilimadjaro = 0
k2 = 0
everest = 0
total_number_participants = 0

for _ in range(groups_participants):
    number_of_participants = int(input())
    if number_of_participants <= 5:
        musala += number_of_participants
        total_number_participants += number_of_participants
    elif 6 <= number_of_participants <= 12:
        montblanc += number_of_participants
        total_number_participants += number_of_participants
    elif 13 <= number_of_participants <= 25:
        kilimadjaro += number_of_participants
        total_number_participants += number_of_participants
    elif 26 <= number_of_participants <= 40:
        k2 += number_of_participants
        total_number_participants += number_of_participants
    elif 41 <= number_of_participants:
        everest += number_of_participants
        total_number_participants += number_of_participants

musala_percentage = (musala / total_number_participants) * 100
montblanc_percentage = (montblanc / total_number_participants) * 100
kilimadjaro_percentage = (kilimadjaro / total_number_participants) * 100
k2_percentage = (k2 / total_number_participants) * 100
everest_percentage = (everest / total_number_participants) * 100

print(f'{musala_percentage:.2f}%')
print(f'{montblanc_percentage:.2f}%')
print(f'{kilimadjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')