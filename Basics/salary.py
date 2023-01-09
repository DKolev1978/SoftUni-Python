n = int(input())
salary = float(input())

first_salary = salary

for i in range(1, n + 1):
    if first_salary > 0:
        web = input()

        if web == "Facebook":
            first_salary = first_salary - 150
        elif web == "Instagram":
            first_salary = first_salary - 100
        elif web == "Reddit":
            first_salary = first_salary - 50

if first_salary == 0:
    print("You have lost your salary.")
else:
    print(int(first_salary))



