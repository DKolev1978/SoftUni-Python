file_path = [file_mame for file_mame in input().split("\\")]
file_args = file_path[-1]


file_mame = file_args.split(".")
file_type = file_mame.pop()


print(f"File name: {'.'.join(file_mame)}")
print(f"File extension: {file_type}")

