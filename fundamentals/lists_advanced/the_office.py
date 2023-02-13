employees_happiness = [int(num) for num in input().split()]
factor = int(input())
happy_count = 0
total_count = len(employees_happiness)
list_average_happiness = list(map(lambda x: x*factor, employees_happiness))
average_happiness = sum(list_average_happiness) / len(employees_happiness)
for person in range(len(employees_happiness)):
    if employees_happiness[person] >= average_happiness:
        happy_count += 1


print(f"Score: {happy_count}/{total_count}. Employees are happy!")
print(average_happiness)