def palindrome_checker(list_palindrome):
    for num in list_palindrome:
        is_palindrome = num[0] == num[-1]
        if is_palindrome:
            print("True")
        else:
            print("False")


positive_ints = input().split(", ")
palindrome_checker(positive_ints)