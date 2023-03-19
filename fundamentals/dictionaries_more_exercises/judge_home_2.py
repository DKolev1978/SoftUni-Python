contest_score = {}
user_score = {}

info = input()

while info != "no more time":
    username, contest, points = info.split(" -> ")
    points = int(points)

    user_score[username] = user_score.get(username, 0)
    if username not in contest_score.get(contest, ""):
        user_score[username] += points
    if contest not in contest_score:
        contest_score[contest] = {username: points}
    if username in contest_score[contest]:
        contest_score[contest][username] = max(contest_score[contest][username], points)
        user_score[username] = max(user_score[username], points)

    contest_score[contest][username] = points

    info = input()


for k, v in contest_score.items():
    print(f"{k}: {len(contest_score[k])} participants")
    for position, (user, score) in enumerate(sorted(v.items(), key=lambda v: (-v[1], v[0])), 1):
        print(f"{position}. {user} <::> {score}")

print("Individual standings:")
for pos, (user, score) in enumerate(sorted(user_score.items(), key=lambda k: (-k[1], k[0])), 1):
    print(f"{pos}. {user} -> {score}")
