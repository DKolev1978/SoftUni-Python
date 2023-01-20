n = int(input())
capacity = 255
litters = 0
while n > 0:
    litters_in = int(input())
    n -= 1
    if capacity < litters_in:
        print("Insufficient capacity!")
        continue
    capacity -= litters_in
    litters += litters_in

print(litters)