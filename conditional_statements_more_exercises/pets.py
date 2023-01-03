from math import floor, ceil
days = int(input())                 # days of vacancy
food = int(input())                 # kg
dog_daily_food = float(input())     # kg
cat_daily_food = float(input())     # kg
turtle_daily_food = float(input())  # g

dog_food = days * dog_daily_food
cat_food = days * cat_daily_food
turtle_food = days * turtle_daily_food / 1000
total_food_eaten = dog_food + cat_food + turtle_food
diff = abs(food - total_food_eaten)

if food >= total_food_eaten:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')


