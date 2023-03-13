users_by_side = {}
side_by_users = {}

while True:
    user_input = input()
    if user_input == "Lumpawaroo":
        break

    if " | " in user_input:
        force_side, force_user = user_input.split(" | ")
        if force_side not in users_by_side:
            users_by_side[force_side] = []

        if force_user not in side_by_users:
            side_by_users[force_user] = force_side
            users_by_side[force_side].append(force_user)
    else:
        force_user, force_side = user_input.split(" -> ")
        if force_side not in users_by_side:
            users_by_side[force_side] = []

        users_by_side[force_side].append(force_user)
        if force_user in side_by_users:
            old_side = side_by_users[force_user]
            users_by_side[old_side].remove(force_user)
            side_by_users[force_user] = force_side
        else:
            side_by_users[force_user] = force_side
        print(f"{force_user} joins the {force_side} side!")


for side, members in users_by_side.items():
    if len(members) == 0:
        continue

    print(f"Side: {side}, Members: {len(members)}")
    for member in members:
        print(f"! {member}")

