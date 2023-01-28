cards = input().split()
shuffle_count = int(input())

for _ in range(shuffle_count):
    first_part = []
    second_part = []
    for idx in range(1, len(cards) - 1):
        card = cards[idx]
        if idx < len(cards) / 2:
            first_part.append(card)
        else:
            second_part.append(card)
    shuffled = []
    first_part_idx = 0
    second_part_idx = 0
    for idx in range(len(first_part) * 2):
        if idx % 2 == 0:
            shuffled.append(second_part[second_part_idx])
            second_part_idx += 1
        else:
            shuffled.append(first_part[first_part_idx])
            first_part_idx += 1
    cards = [cards[0]] + shuffled + [cards[-1]]
print(cards)

# one two three four