user_input = input().split()

for num in range(len(user_input)):
    user_input[num] = int(user_input[num]) * -1

print(user_input)

