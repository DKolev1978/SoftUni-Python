input_list = [int(x) for x in input().split(", ")]
index_list = [idx for idx in range(len(input_list)) if input_list[idx] % 2 == 0]
print(index_list)