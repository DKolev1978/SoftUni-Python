contest_password = {}
contest_users = {}
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
            contest_users[contest] = {username: points}
            if contest_users[contest][username] < points:
                contest_users[contest][username] = points
            # if contest_users[contest][username] > points:
            #     pass
            # else:
            #     contest_users[contest][username] = points
            print(contest_users[contest][username])
    #  "{contest}=>{password}=>{username}=>{points}"

    user_input = input()
print(contest_password)
print(contest_users)





