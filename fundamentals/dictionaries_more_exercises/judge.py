contests_by_user_points = {}
users_contests_points = {}
user_input = input()

while user_input != "no more time":
    username, contest, points = user_input.split(" -> ")
    points = int(points)
    if username not in contests_by_user_points:
        contests_by_user_points[username] = {}
    if contest not in contests_by_user_points[username]:
        contests_by_user_points[username][contest] = points
    elif points > contests_by_user_points[username][contest]:
        contests_by_user_points[username][contest] = points
    if contest not in users_contests_points:
        users_contests_points[contest] = {}
    if username not in users_contests_points:
        users_contests_points[contest][username] = points
    elif points > users_contests_points[contest][username]:
        users_contests_points[contest][username] = points

    user_input = input()


print(contests_by_user_points)
print(users_contests_points)
