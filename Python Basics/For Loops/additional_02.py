period = int(input())

doctors = 7
untreated_clients = 0
treated_clients = 0

for current_day in range(1, period + 1):
    daily_clients = int(input())
    if current_day % 3 == 0 and untreated_clients > treated_clients:
        doctors += 1
    if daily_clients <= doctors:
        treated_clients += daily_clients
    elif daily_clients > doctors:
        untreated_clients += (daily_clients - doctors)
        treated_clients += doctors


print(f'Treated patients: {treated_clients}.')
print(f'Untreated patients: {untreated_clients}.')