puppy_food_kg = int(input())
input_line = input()
puppy_food_gr = puppy_food_kg * 1000
food_eat = 0
while input_line != "Adopted":
    puppy_eat = int(input_line)
    food_eat += puppy_eat
    input_line = input()

diff = abs( puppy_food_gr - food_eat )
if puppy_food_gr < food_eat:
    print(f"Food is not enough. You need {diff} grams more.")
else:
    print(f"Food is enough! Leftovers: {diff} grams.")