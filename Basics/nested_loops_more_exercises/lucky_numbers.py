n = int(input())

for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            for m in range(1, n):
                if i + j == k + m:
                    if n % (i + j) == 0:
                        print(f"{i}{j}{k}{m}", end=" ")
