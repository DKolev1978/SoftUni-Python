n = int(input())
positive_numbers = []
negative_numbers = []
for i in range(n):
    number = int(input())
    if number < 0:
        negative_numbers.append(number)
    else:
        positive_numbers.append(number)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}\nSum of negatives: {sum(negative_numbers)}")

