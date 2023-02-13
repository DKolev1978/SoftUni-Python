x = [num for num in range(5)]

print(x)

nums = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in nums]
print(f"squares {squares}")

evens = [num for num in nums if num % 2 == 0]
filtered = [True if x % 2 == 0 else False for x in nums]
print(f"Evens {evens}")
print(f"Filtered {filtered}")

my_list = [1, 2, 3]

# my_list.append(4)
# my_list.extend([4, 5])
# my_list.insert(1, 4)
# my_list.clear()
# my_list.pop(0)
my_list.remove(1)
print(f"my_list {my_list}")

