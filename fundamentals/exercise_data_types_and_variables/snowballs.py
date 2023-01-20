count = int(input())

snowball_weight = 0
snowball_time = 0
snowball_quality = 0
max_snowball_value = float("-inf")
output = ""
for i in range(count):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int((snowball_weight / snowball_time) ** snowball_quality)
    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        output = f"{snowball_weight} : {snowball_time} = {max_snowball_value} ({snowball_quality})"

print(output)