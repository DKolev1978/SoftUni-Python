def decimalToBinary(n):
    return bin(n).replace("0b", "")


def counter(number, par):
    count = 0
    for i in number:
        if int(i) == par:
            count += 1
    return count


n = int(input())
b = int(input())
number = decimalToBinary(n)
print(counter(number, b))
