import os

root_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "my_first_file.txt"
file_path = os.path.join(root_dir,file_name)

if os.path.isfile(file_path):
    os.remove('my_first_file.txt')
# except FileNotFoundError:
#     print("File already deleted!")
