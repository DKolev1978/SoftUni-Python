n = int(input())

p_1, p_2, p_3, p_4, p_5 = 0, 0, 0, 0, 0


for i in range(1, n +1):
    current_num = int(input())

    if current_num < 200:
        p_1 += 1
    elif current_num <= 399:
        p_2 += 1
    elif current_num <= 599:
        p_3 += 1
    elif current_num <= 799:
        p_4 += 1
    elif current_num >= 800:
        p_5 += 1
print(f'{p_1 / n * 100:.2f}%')
print(f'{p_2 / n * 100:.2f}%')
print(f'{p_3 / n * 100:.2f}%')
print(f'{p_4 / n * 100:.2f}%')
print(f'{p_5 / n * 100:.2f}%')