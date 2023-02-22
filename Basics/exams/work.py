import random, msvcrt
m = 101
prokredit, ubb_interleas = 0, 0
while m > 0:
    m -= 1
    n = random.randint(0, 1)
    if n == 0:
        result = "Prokredit"
        prokredit += 1
        continue

    elif n == 1:
        result = "UBB Interlease"
        ubb_interleas += 1
        continue


print(f"{prokredit} for ProKredit")
print(f"{ubb_interleas} for UBB Interlease")



