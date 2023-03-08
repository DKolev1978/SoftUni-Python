# n = int(input())
# b = int(input())
# counter = 0
# while n > 0:
#     if n % 2 == b:
#         counter += 1
#     n = n // 2
# print(counter)
#
#
def decimalToBinary(n):
    return bin(n).replace("0b", "")


n = int(input())
result = decimalToBinary(n)

bitAtPosition1 = result[len(result) - 2]

print(bitAtPosition1)



