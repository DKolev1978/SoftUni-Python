n = int(input())

for num in range(1, n+1):
    sum = 0
    digit = num

    while digit:
        sum += digit % 10
        digit = int(digit / 10)

    if sum == 5 or sum == 7 or sum == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
