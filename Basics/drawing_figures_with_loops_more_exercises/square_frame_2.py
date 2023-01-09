n = int(input())
middle = "- "
corner = "+ "
side = "| "

print(corner + (n-2) * middle + corner)
for row in range(1, n - 1):
    print(side + (n - 2) * middle + side)
print(corner + (n - 2) * middle + corner)



