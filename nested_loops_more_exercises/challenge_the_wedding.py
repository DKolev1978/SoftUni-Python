men_count = int(input())
women_count = int(input())
tables_count = int(input())

for men in range(1, men_count + 1):
    for women in range(1, women_count + 1):
        if tables_count == 0:
            break
        print(f"({men} <-> {women})", end=" ")
        tables_count -= 1