x1, x2, x3 = [int(x) for x in input().split('.')]
x3 += 1

if x3 == 10:
    x3 = 0
    x2 += 1

    if x2 == 10:
        x2 = 0
        x1 += 1
print(f"{x1}.{x2}.{x3}")