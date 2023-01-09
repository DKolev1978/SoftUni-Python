n1 = int(input())
n2 = int(input())

for number in range(n1, n2 + 1):
    number_str = str(number)
    even_sum = 0
    odd_sum = 0
    for j in range(0, len(number_str)):
        digit = int(number_str[j])
        if j % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(number_str, end=' ')


