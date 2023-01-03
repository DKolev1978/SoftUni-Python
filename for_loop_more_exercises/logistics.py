number_of_loads = int(input())

total_tons = 0
van_tons = 0
truck_tons = 0
train_tons = 0
price = 0
for i in range(number_of_loads):
    input_tons = int(input())
    if input_tons <= 3:
        price += input_tons * 200
        total_tons += input_tons
        van_tons += input_tons
    elif 3 < input_tons <= 11:
        price += input_tons * 175
        total_tons += input_tons
        truck_tons += input_tons
    else:
        price += input_tons * 120
        total_tons += input_tons
        train_tons += input_tons

av_price = price / total_tons
prc_van = van_tons / total_tons * 100
prc_truck = truck_tons / total_tons * 100
prc_train = train_tons / total_tons * 100
print(f"{av_price:.2f}")
print(f"{prc_van:.2f}%")
print(f"{prc_truck:.2f}%")
print(f"{prc_train:.2f}%")



