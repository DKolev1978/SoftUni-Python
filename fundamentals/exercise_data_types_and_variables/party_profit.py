companions_count = int(input())
days = int(input())
coins = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        companions_count -= 2
    if i % 15 == 0:
        companions_count += 5
        coins -= 2 * companions_count

    coins += 50
    coins -= 2 * companions_count
    if i % 3 == 0:
        coins -= 3 * companions_count
    if i % 5 == 0:
        coins += 20 * companions_count

coins_per_companion = coins // companions_count
print(f"{companions_count} companions received {coins_per_companion} coins each.")