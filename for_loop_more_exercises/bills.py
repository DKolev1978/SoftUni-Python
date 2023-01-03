months = int(input())

electricity_bill = 0
water_bill = 0
internet_bill = 0
other_bill = 0

for i in range(months):
    electricity = float(input())
    electricity_bill += electricity
    water_bill += 20
    internet_bill += 15
    other_bill = electricity_bill + water_bill + internet_bill + (electricity_bill + water_bill + internet_bill) * 0.2

all_expenses = electricity_bill + water_bill + internet_bill + other_bill

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {other_bill:.2f} lv")
print(f"Average: {all_expenses / months:.2f} lv")
