# negative_numbers = []
# positive_numbers = list([int(x) if int(x) > 0 else negative_numbers.append(int(x)) for x in input().split()])
# print(negative_numbers)
# print(positive_numbers)
# numbers = [int(x) for x in input().split()]
# negative_numbers = []
# positive_numbers = []
# for num in numbers:
#     if num > 0:
#         positive_numbers.append(num)
#     else:
#         negative_numbers.append(num)
#
# print(sum(negative_numbers))
# print(sum(positive_numbers))
#
# if abs(sum(negative_numbers)) > abs(sum(positive_numbers)):
#     print("The negatives are stronger than the positives")
# else:
#     print("The positives are stronger than the negatives")

def print_numbers(positive, negative):
    print(negative)
    print(positive)
    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
positive_numbers = sum(x for x in numbers if x > 0)
negative_numbers = sum(x for x in numbers if x <= 0)

print_numbers(positive_numbers, negative_numbers)