import os

# with open('my_first_file.txt', 'w') as file:
#     file.write('I just created my first file!')
# with open('my_first_file.txt', 'r')as file:
#     print(file.readline())

root_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_dir, "my_first_file.txt")

with open(file_path, "w") as file:
    file.write('I just created my first file!')
