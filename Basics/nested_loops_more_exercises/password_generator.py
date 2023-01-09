n = int(input())
last_symbol = int(input())

for i in range(1, n):
    for j in range(1, n):
        for l in range(97, 97 + last_symbol):
            for k in range(97, 97 + last_symbol):
                for m in range(1, n + 1):
                    if m > i and m > j:
                        print(f"{i}{j}{chr(l)}{chr(k)}{m}", end=" ")


