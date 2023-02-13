def even(x):
    return x % 2 == 0


nums = [int(n) for n in input().split()]


print(list(filter(even, nums)))