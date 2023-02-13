numbers = input()
nums = [int(n) for n in numbers.split(", ")]

for num in nums:
    list_of_digits = [int(i) for i in str(num)]
    if list_of_digits[0] == list_of_digits[-1]:
        print("True")
    else:
        print("False")
