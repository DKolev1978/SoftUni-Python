population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())
is_possible = False
for index in range(len(population)):
    idx = population[index]
    max_index = population.index(max(population))
    if sum(population) // len(population) < minimum_wealth:
        is_possible = True
        break
    if idx < minimum_wealth:
        added_points = minimum_wealth - idx
        population[index] += added_points
        population[max_index] -= added_points

if is_possible:
    print("No equal distribution possible")
else:
    print(population)

