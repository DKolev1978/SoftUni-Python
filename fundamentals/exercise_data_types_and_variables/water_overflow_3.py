n = int(input())
capacity = 255
litters = 0
for _ in range(n):
    litters_in = int(input())

    if litters + litters_in > capacity:
        print("Insufficient capacity!")
    else:
        litters += litters_in
print(litters)