import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolute_path, "numbers.txt")
file = open(file_path)
print(sum(int(x) for x in file if x))
