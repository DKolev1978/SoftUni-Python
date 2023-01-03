n = int(input())

sum_odd = 0
sum_even = 0
for i in range(1, n + 1):
    numbers = int(input())
    if i % 2 != 0:
        sum_odd += numbers
    else:
        sum_even += numbers

diff = abs(sum_odd - sum_even)

if sum_odd == sum_even:
    print("Yes")
    print(f'Sum = {sum_odd}')
else:
    print("No")
    print(f'Diff = {diff}')