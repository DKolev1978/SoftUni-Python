from math import ceil, floor
n = int(input())

print((2 * n) * "*" + n * " " + (2 * n) * "*")
for i in range(n - 2):
    if floor((n - 1) / 2 - 1) == i:
        print("*" + (2 * n - 2) * "/" + "*" + n * "|" + "*" + (2 * n - 2) * "/" + "*")
    else:
        print("*" + (2 * n - 2) * "/" + "*" + n * " " + "*" + (2 * n - 2) * "/" + "*")
print((2 * n) * "*" + n * " " + (2 * n) * "*")
