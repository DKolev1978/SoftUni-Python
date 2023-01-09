import sys
numbers = int(input())

odd_min = sys.maxsize
odd_max = -sys.maxsize
odd_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
even_sum = 0

for i in range(1, numbers + 1):
    input_number = float(input())
    if i % 2 != 0:
        odd_sum += input_number
        if input_number <= odd_min:
            odd_min = input_number
        if input_number >= odd_max:
            odd_max = input_number
    else:
        even_sum += input_number
        if input_number <= even_min:
            even_min = input_number
        if input_number >= even_max:
            even_max = input_number
        if i == 0:
            even_max = str("No")
            even_min = str("No")

print(f"OddSum={odd_sum:.2f},")
if numbers == 0:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if numbers == 0:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if numbers == 0:
    print(f"EvenMin=No,")
elif numbers == 1:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")

if numbers == 0:
    print(f"EvenMax=No")
elif numbers == 1:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")
