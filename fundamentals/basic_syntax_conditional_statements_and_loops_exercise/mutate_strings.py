first = input()
second = input()

result = ""

for w in range(len(first)):
    if first[w] == second[w]:
        continue

    result = second[:w + 1] + first[w + 1:]
    print(result)