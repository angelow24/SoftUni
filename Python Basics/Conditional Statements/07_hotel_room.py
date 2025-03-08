# За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# · За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# · За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# · За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

month = input()  # May, June, July, August, September or October
number_of_nights = int(input())

discount = 0
studio_discount = 0
apartment_discount = 0

if month == 'May' or month == 'October':
    if number_of_nights > 7:
        studio_discount = 0.05
    if number_of_nights > 14:
        studio_discount = 0.30
elif month == 'June' or month == 'September':
    if number_of_nights > 14:
        studio_discount = 0.20
if number_of_nights > 14:
    apartment_discount = 0.10

if month == 'May' or month == 'October':
    studio_price = 50 * number_of_nights * (1 - studio_discount)
    apartment_price = 65 * number_of_nights * (1 - apartment_discount)
elif month == 'June' or month == 'September':
    studio_price = 75.20 * number_of_nights * (1 - studio_discount)
    apartment_price = 68.70 * number_of_nights * (1 - apartment_discount)
elif month == 'July' or month == 'August':
    studio_price = 76.00 * number_of_nights * (1 - studio_discount)
    apartment_price = 77.00 * number_of_nights * (1 - apartment_discount)

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')



