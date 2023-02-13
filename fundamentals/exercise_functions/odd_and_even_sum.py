def odd_or_even_calculate(a):
    list_of_digits = [int(i) for i in str(numbers)]
    sum_odd, sum_even = 0, 0
    for num in range(len(list_of_digits)):
        new_num = int(list_of_digits[num])
        if new_num % 2 == 0:
            sum_even += new_num
        else:
            sum_odd += new_num

    print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")


numbers = int(input())

odd_or_even_calculate(numbers)
# #
# #
# # # Python3 implementation of the approach
# #
# # # Function to return the
# # # reverse of a number
# # def reverse(n):
# #     rev = 0
# #     while (n != 0):
# #         rev = (rev * 10) + (n % 10)
# #         n //= 10
# #     return rev
# #
# #
# # # Function to find the sum of the odd
# # # and even positioned digits in a number
# # def getSum(n):
# #     n = reverse(n)
# #     sumOdd = 0
# #     sumEven = 0
# #     c = 1
# #
# #     while (n != 0):
# #
# #         # If c is even number then it means
# #         # digit extracted is at even place
# #         if (c % 2 == 0):
# #             sumEven += n % 10
# #         else:
# #             sumOdd += n % 10
# #         n //= 10
# #         c += 1
# #
# #     print("Sum odd =", sumOdd)
# #     print("Sum even =", sumEven)
# #
# #
# # # Driver code
# # n = int(input())
# # getSum(n)
# #
# # # This code is contributed
# # # by mohit kumar
# # Python3 implementation of the approach
#
# # Function to find the sum of the odd
# # and even positioned digits in a number
# def getSum(n):
#     # If n is odd then the last digit
#     # will be odd positioned
#     if (n % 2 == 1):
#         isOdd = True
#     else:
#         isOdd = False
#
#     # To store the respective sums
#     sumOdd = 0
#     sumEven = 0
#
#     # While there are digits left process
#     while (n != 0):
#
#         # If current digit is odd positioned
#         if (isOdd):
#             sumOdd += n % 10
#
#         # Even positioned digit
#         else:
#             sumEven += n % 10
#
#         # Invert state
#         isOdd = not isOdd
#
#         # Remove last digit
#         n //= 10
#
#     print("Sum odd = ", sumOdd)
#     print("Sum even = ", sumEven)
#
#
# # Driver code
# if __name__ == "__main__":
#     n = 1000435
#     getSum(n)
#
# # This code is contributed by chitranayal
