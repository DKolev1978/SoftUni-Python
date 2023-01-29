cards = input().split()
shuffle_count = int(input())
half = len(cards) // 2
l, p, shuffle = cards[:half], cards[half:], list()

for _ in range(shuffle_count):
    for i in range(half):
        shuffle.append(l[i])
        shuffle.append(p[i])
print(shuffle)

# a b c d e f g h
# 5
