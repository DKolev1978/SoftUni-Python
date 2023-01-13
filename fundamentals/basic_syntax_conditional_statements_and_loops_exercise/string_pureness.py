count = int(input())

for _ in range(count):
    wd = input()
    flag = True
    for chr in wd:
        if chr == "." or chr =="," or chr == "_":
            flag = False
            break
    if flag:
        print(f"{wd} is pure.")
    else:
        print(f"{wd} is not pure!")
