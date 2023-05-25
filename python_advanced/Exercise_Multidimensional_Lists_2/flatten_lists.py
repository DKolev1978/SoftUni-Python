# user_input = input().split("|")
#
# flatten_list = []
#
# for el in user_input[::-1]:
#     flatten_list.extend(el.split())
#
# print(*flatten_list)

# solution 2
numbers = [st.split() for st in input().split("|")]
print(*[' '.join(s_l) for s_l in numbers[::-1] if s_l])
