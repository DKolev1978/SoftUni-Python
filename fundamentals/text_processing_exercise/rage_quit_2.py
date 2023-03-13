string = input().upper()
result = ''
unique_chars = set()
last_digit_index = current_digit_index = -1
for i in range(len(string)):
    if string[i].isdigit():
        current_digit_index = i
    if current_digit_index != last_digit_index:
        number_len = 1
        for j in range(i + 1, len(string), 1):
            if not string[j].isdigit():
                break
            number_len += 1
        num = int(string[i:number_len+i])
        text = string[last_digit_index + 1:i]
        if num > 0:
            for v in range(num):
                result += text
            for char in text:
                unique_chars.add(char)
        current_digit_index = current_digit_index + number_len - 1
        last_digit_index = current_digit_index
print(f"Unique symbols used: {len(unique_chars)}")
print(result)