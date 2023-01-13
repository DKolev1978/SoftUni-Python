n = int(input())

for _ in range(n):
    user_input = int(input())
    if user_input == 88:
        print("Hello")
    elif user_input == 86:
        print("How are you?")
    elif user_input < 88:
        print("GREAT!")
    else:
        print("Bye.")
