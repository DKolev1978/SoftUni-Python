number = input()

prime_numbers = 0
complex_numbers = 0
while number != "stop":
    current_number = int(number)
    if current_number < 0:
        print("Number is negative.")
        number = input()
        continue

    prime_count = 0
    for i in range(1, current_number + 1):
        if current_number % i == 0:
            prime_count += 1
    if prime_count == 2:
        prime_numbers += current_number
    else:
        complex_numbers += current_number

    number = input()
print(f"Sum of all prime numbers is: {prime_numbers}")
print(f"Sum of all non prime numbers is: {complex_numbers}")
