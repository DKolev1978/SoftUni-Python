import os


def extensions_func(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split('.')[-1]

            if extension not in extension_dict:
                extension_dict[extension] = []
            extension_dict[extension].append(filename)
        elif os.path.isdir(file) and not first_level:
            extensions_func(file, first_level=True)


directory = input()
extension_dict = {}
extensions_func(directory)

extension_dict = sorted(extension_dict.items(),key = lambda kvpt:kvpt[0])

for exten,files in extension_dict:
    print(f".{exten}")
    for el in sorted(files):
        print(f"- - - {el}")
