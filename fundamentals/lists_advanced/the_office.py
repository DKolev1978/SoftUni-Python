employees_happiness = [int(num) for num in input().split()]
factor = int(input())
happy_count = 0
total_count = len(employees_happiness)
list_average_happiness = list(map(lambda x: x*factor, employees_happiness))
average_happiness = sum(list_average_happiness) / len(employees_happiness)
for person in range(len(list_average_happiness)):
    person_happiness = int(list_average_happiness[person])
    if person_happiness > average_happiness:
        happy_count += 1

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")