from math import log

number = int(input())
base_log = input()

if base_log == "natural":
    print(f"{log(number):.2f}")
else:
    try:
        print(f"{log(number, int(base_log)):.2f}")
    except ValueError:
        print("Enter a valid integer or 'natural'")