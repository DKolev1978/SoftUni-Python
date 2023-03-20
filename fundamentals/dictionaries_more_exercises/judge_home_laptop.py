contest_by_username_and_points = {}

username_by_contest_points = {}

impute_line = input()

while impute_line != "no more time":
    username, contest, points = impute_line.split(" -> ")
    points = int(points)
    if contest not in contest_by_username_and_points:
        contest_by_username_and_points[contest] = {}
    if username not in contest_by_username_and_points:
        contest_by_username_and_points[contest][username] = points
    elif points > contest_by_username_and_points[username][points]:
        contest_by_username_and_points[contest][username] = points

    impute_line = input()

user_score = {}
for k, v in contest_by_username_and_points.items():
    for name, point in v.items():
        if name not in user_score.keys():
            user_score[name] = point
        else:
            user_score[name] += point

for key, value in contest_by_username_and_points.items():
    print(f"{key}: {len(contest_by_username_and_points[key])} participants")
    n = 1
    for k, v in sorted(value.items(), key=lambda x: (-x[1], x[0])):
        print(f"{n}. {k} <::> {value[k]}")
        n += 1

n = 1
user_score_sorted = dict(sorted(user_score.items(), key=lambda item: (-item[1], item[0])))
print("Individual standings:")
for key, value in user_score_sorted.items():
    print(f"{n}. {key} -> {value}")
    n += 1




