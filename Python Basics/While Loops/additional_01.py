bottles_cleaning_product = int(input())
cleaning_product_ml = bottles_cleaning_product * 750
day = 0
saucepan_cleaned = 0
plate_cleaned = 0

while True:
    command = input()
    day += 1

    if command == 'End':
        print(f'Detergent was enough!')
        print(f'{plate_cleaned} dishes and {saucepan_cleaned} pots were washed.')
        print(f'Leftover detergent {cleaning_product_ml} ml.')
        break

    tableware_for_cleaning = int(command)

    if day % 3 == 0:
        cleaning_product_ml -= tableware_for_cleaning * 15
        saucepan_cleaned += tableware_for_cleaning
    else:
        cleaning_product_ml -= tableware_for_cleaning * 5
        plate_cleaned += tableware_for_cleaning
    if cleaning_product_ml <= 0:
        print(f'Not enough detergent, {abs(cleaning_product_ml)} ml. more necessary!')
        break





