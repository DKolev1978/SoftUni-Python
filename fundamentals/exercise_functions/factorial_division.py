def fac_calculation(n):
    fac = 1
    for i in range(n, 0, -1):
        fac = fac * i
    return fac


input_number_one = int(input())
input_number_two = int(input())
result = fac_calculation(input_number_one) / fac_calculation(input_number_two)
print(f"{result:.2f}")