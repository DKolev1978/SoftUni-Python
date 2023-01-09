inherited_money = float(input())
year = int(input())
year_back_in_time = 1800
gosho_years = 18
spend_money = 0
total_spend_money = 0
for i in range(year_back_in_time, year + 1):
    if i % 2 == 0:
        spend_money = 12000
    else:
        spend_money = 12000 + gosho_years * 50
    total_spend_money += spend_money
    gosho_years += 1
diff = abs(total_spend_money - inherited_money)
if inherited_money >= total_spend_money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left." )
else:
    print(f"He will need {diff:.2f} dollars to survive.")

