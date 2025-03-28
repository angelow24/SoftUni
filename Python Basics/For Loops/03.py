counter = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for _ in range(counter):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif 200 <= current_number <= 399:
        p2 += 1
    elif 400 <= current_number <= 599:
        p3 += 1
    elif 600 <= current_number <= 799:
        p4 += 1
    elif 800 <= current_number:
        p5 += 1

p1_percentage = (p1 / counter) * 100
p2_percentage = (p2 / counter) * 100
p3_percentage = (p3 / counter) * 100
p4_percentage = (p4 / counter) * 100
p5_percentage = (p5 / counter) * 100

print(f'{p1_percentage:.2f}%')
print(f'{p2_percentage:.2f}%')
print(f'{p3_percentage:.2f}%')
print(f'{p4_percentage:.2f}%')
print(f'{p5_percentage:.2f}%')