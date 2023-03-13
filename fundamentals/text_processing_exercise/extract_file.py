file_path = [file_mame for file_mame in input().split("\\")]
file_args = file_path[-1].split(".")
file_mame = file_args[0]
file_type = file_args[1]

print(f"File name: {file_mame}")
print(f"File extension: {file_type}")