n = int(input())
capacity = 255
litters = 0
for _ in range(n):
    litters_in = int(input())

    if capacity < litters_in:
        print("Insufficient capacity!")
        continue
    capacity -= litters_in
    litters += litters_in

print(litters)
