text = input()

a = 0
e = 0
i = 0
o = 0
u = 0

for word in text:
    if word == 'a':
        a += 1
    if word == 'e':
        e += 2
    if word == 'i':
        i += 3
    if word == 'o':
        o += 4
    if word == 'u':
        u += 5

total_sum = (a + e + i + o + u)

print(total_sum)