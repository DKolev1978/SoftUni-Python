import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
try:
    file_path = os.path.join(absolute_path, "text.txt")
    file = open(file_path)
    print('File found')
except FileNotFoundError:
    print('File not found')


