nums = input()
nums_to_remove = int(input())
nums_int = [int(x) for x in nums.split(" ")]
for num in range(nums_to_remove):
    min_number = min(nums_int)
    nums_int.remove(min_number)

print(", ".join([str(x) for x in nums_int]))



