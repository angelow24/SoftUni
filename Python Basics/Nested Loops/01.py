n = int(input("Въведете цяло число: "))

current = 1
is_finished = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if current > n:
            is_finished = True
            break

        print(current, end=" ")
        current += 1

    if is_finished:
        break

    print()  # Нов ред след всяко завършено ниво на пирамидата
