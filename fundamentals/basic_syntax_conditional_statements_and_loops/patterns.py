number = int(input())

for num in range(1, number + 1):
    for j in range(num):
        print("*", end="")
    print()
for num in range(number - 1, 0, -1):
    for j in range(num):
        print("*", end="")
    print()