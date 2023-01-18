number = input()

string = []

for i in number:
    string.append(int(i))

while 0 < len(string):
    max_index = (max(string))
    print(max_index, end='')
    string.remove(max(string))
