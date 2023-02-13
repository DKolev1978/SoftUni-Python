words = input().split()

result = list(filter(lambda x: len(x) % 2 == 0, words))

print("\n".join(result))