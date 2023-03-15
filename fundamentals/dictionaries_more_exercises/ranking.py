contest_password = {}
contest_users = {}
user_input = input()
best_students = {}
total_points = 0
sum_points = 0
while True:
    if user_input == "end of contests":
        break

    contest, password = user_input.split(":")
    contest_password[contest] = password
    user_input = input()

user_input = input()
while True:
    if user_input == "end of submissions":
        break
    contest, password, username, points = user_input.split("=>")
    points = int(points)
    if contest in contest_password:
        if password == contest_password[contest]:
            username_score = {username: points}
            if contest not in contest_users:
                contest_users[contest] = username_score
            else:
                contest_users[contest].update(username_score)
                for key, value in contest_users.items():
                    for k, v in value.items():
                        if v < points:
                            v = points

    user_input = input()

for key, value in contest_users.items():
    if value and username in value.keys():
        sum_points += value[username]
        best_students =
print(sum_points)


print(contest_users)

# # Python code to find sum values within nested dictionaries
# weapons = {'': None, 'sword': {'steel': 151,
#                                'sharpness': 100,
#                                'age': 2, },
#
#            'arrow': {'steel': 120,
#                      'sharpness': 205,
#                      'age': 1, }}
#
# sumValue1 = sum(d['sharpness'] for d in weapons.values() if d)
# sumValue2 = sum(d['steel'] for d in weapons.values() if d)
#
# print(sumValue1)
# print(sumValue2)
