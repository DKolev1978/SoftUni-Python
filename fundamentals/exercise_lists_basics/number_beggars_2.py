user_input = input().split(", ")
beggars_count = int(input())
beggars = [0] * beggars_count

for idx in range(len(user_input)):
    beggar_idx = idx % beggars_count
    num = int(user_input[idx])
    beggars[beggar_idx] += num

print(beggars)