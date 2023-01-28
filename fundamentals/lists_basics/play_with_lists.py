# numbers = [1, 2, 3, 4]
# print(numbers)
#
# numbers.remove(numbers[0])
# print(numbers)
#
zoo = ["cat", "dog", "parrot"]
#
# for idx in range(len(zoo)):
#     print(idx, zoo[idx])
#
while zoo:

    print(zoo)
    new_zoo = zoo[0]
    zoo.remove(new_zoo)
print(zoo)