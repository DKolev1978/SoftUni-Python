from collections import OrderedDict
import operator

contest_password = {}
contest_by_users_points = {}
users_by_contests_points = {}
user_input = input()

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
            if contest not in contest_by_users_points:
                contest_by_users_points[contest] = {username: points}
                if contest_by_users_points[contest][username] < points:
                    contest_by_users_points[contest][username] = points
            elif username not in contest_by_users_points[contest]:
                contest_by_users_points[contest].update({username: points})
            if username not in users_by_contests_points:
                users_by_contests_points[username] = {contest: points}
                if users_by_contests_points[username][contest] < points:
                    users_by_contests_points[username][contest] = points
            elif contest not in users_by_contests_points[username]:
                users_by_contests_points[username].update({contest: points})
    user_input = input()
res = {key: sum(d.get(key, 0) for d in contest_by_users_points.values()) for key in set().union(*contest_by_users_points.values())}
best_user = max(res.items())
print(f"Best candidate is {best_user[0]} with total {best_user[1]} points.")
print("Ranking:")
users_by_contests_points = dict(sorted(users_by_contests_points.items()))

for key, value in users_by_contests_points.items():
    print(f"{key}")
    sorted_value = dict(sorted(value.items(), key=operator.itemgetter(1), reverse=True))
    sorted_values = dict(sorted_value)
    for k, v in sorted_values.items():
        print(f"#  {k} -> {v}")





