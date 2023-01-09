n1 = int(input())   # upper border of hundred
n2 = int(input())   # upper border of decimals
n3 = int(input())   # upper border of firsts

for num1 in range(1, n1 + 1):
    if num1 % 2 == 0:
        for num2 in range(2, n2 + 1):
            if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                for num3 in range(1, n3 + 1):
                    if num3 % 2 == 0:
                        print(f"{num1} {num2} {num3}")

