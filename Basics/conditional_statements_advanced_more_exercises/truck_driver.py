season = input()
kilometers = float(input())

price_kilometers = 0
salary = 0

if season == "Spring" or season == "Autumn":
    if kilometers <= 5000:
        price_kilometers = kilometers * 0.75
    elif kilometers <= 10000:
        price_kilometers = kilometers * 0.95
    elif 10000 < kilometers <= 20000:
        price_kilometers = kilometers * 1.45
elif season == "Summer":
    if kilometers <= 5000:
        price_kilometers = kilometers * 0.90
    elif kilometers <= 10000:
        price_kilometers = kilometers * 1.10
    elif 10000 < kilometers <= 20000:
        price_kilometers = kilometers * 1.45
elif season == "Winter":
    if kilometers <= 5000:
        price_kilometers = kilometers * 1.05
    elif kilometers <= 10000:
        price_kilometers = kilometers * 1.25
    elif 10000 < kilometers <= 20000:
        price_kilometers = kilometers * 1.45

salary = price_kilometers * 4
salary_after_taxes = salary - salary * 0.1
print(f"{salary_after_taxes:.2f}")
