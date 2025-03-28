# До 3 тона – микробус (200 лева на тон)
# От 4 до 11 тона – камион (175 лева на тон)
# 12 и повече тона – влак (120 лева на тон)
total_stock_for_transportation = int(input())

bus_load = 0
truck_load = 0
train_load = 0
total_tons_transported = 0

for _ in range(total_stock_for_transportation):
    weight = int(input())
    if weight <= 3:
        bus_load += weight
        total_tons_transported += weight
    elif 4 <= weight <= 11:
        truck_load += weight
        total_tons_transported += weight
    elif 12 <= weight:
        train_load += weight
        total_tons_transported += weight

transportation_cost_bus = bus_load * 200
transportation_cost_truck = truck_load * 175
transportation_cost_train = train_load * 120
average_cost_for_transportation = (transportation_cost_truck + transportation_cost_train +
                                   transportation_cost_bus) / total_tons_transported

average_transported_weight_bus = (bus_load / total_tons_transported) * 100
average_transported_weight_truck = (truck_load / total_tons_transported) * 100
average_transported_weight_train = (train_load / total_tons_transported) * 100

print(f'{average_cost_for_transportation:.2f}')
print(f'{average_transported_weight_bus:.2f}%')
print(f'{average_transported_weight_truck:.2f}%')
print(f'{average_transported_weight_train:.2f}%')

