import os

while True:
    command, *info = input().split("-")

    if command == "Create":
        with open(f"files/{info[0]}", "w"):
            pass

    elif command == "Add":
        with open(f"files/{info[0]}", "a") as file_manipulator_file:
            file_manipulator_file.write(f"{info[1]}\n")

    elif command == "Replace":
        try:
            with open(f"files/{info[0]}", "r+") as file_manipulator_file:
                text = file_manipulator_file.read()
                text = text.replace(info[1], info[2])
                file_manipulator_file.seek(0)
                file_manipulator_file.write(text)

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(f"files/{info[0]}")
        except FileNotFoundError:
            print("An error occurred")

    elif command == "End":
        break