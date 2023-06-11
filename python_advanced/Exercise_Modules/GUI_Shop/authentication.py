from tkinter import Button, Entry
from helpers import clean_screen
from canvas import root, frame
from json import loads, dump


def render_entry():
    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        width=20,
        borderwidth=0,
        height=3,
        command=register
    )

    login_button = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        width=20,
        height=3
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 320, window=login_button)


def get_users_data():
    info_data = []

    with open("db/user_information.txt", "r") as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def register():
    clean_screen()

    frame.create_text(100, 50, text="First name")
    frame.create_text(100, 100, text="Last name")
    frame.create_text(100, 150, text="Username")
    frame.create_text(100, 200, text="Password")

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        borderwidth=0,
        command=registration
    )

    frame.create_window(300, 250, window=register_button)


def registration():
    info_dict = {
        "First name": first_name_box.get(),
        "Last name": last_name_box.get(),
        "Username": username_box.get(),
        "Password": password_box.get(),
    }

    if check_registration(info_dict):
        with open("db/user_information.txt", "r") as users_file:
            dump(info_dict, users_file)
            users_file.write("\n")
            # TODO: Display products


def check_registration(info):
    frame.delete("error")
    for key, value in info.items():
        if not value.strip():
            frame.create_text(
                300,
                300,
                text=f"{key} cannot be empty!",
                fill="red",
                tags="error",
            )

            return False

    info_data = get_users_data()

    for record in info_data:
        if record["Username"] == info["Username"]:
            frame.create_text(
                300,
                300,
                text=f"Username is already taken!",
                fill="red",
                tags="error",
            )

            return False
    return True


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show="*")
