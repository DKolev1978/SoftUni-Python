n = int(input())

while n > 0:
    user_input = int(input())
    n -= 1
    if user_input == 88:
        print("Hello")
    elif user_input == 86:
        print("How are you?")
    elif user_input < 88:
        print("GREAT!")
    else:
        print("Bye.")

