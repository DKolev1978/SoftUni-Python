input_number = float(input())

while input_number >= 0:
    result = input_number * 2
    print(f"Result: {result:.2f}")
    input_number = float(input())
    if input_number < 0:
        print("Negative number!")

