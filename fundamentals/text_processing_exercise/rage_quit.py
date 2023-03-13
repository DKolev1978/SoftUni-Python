text = input().upper()
unique_cont = len(set([letter for letter in text if not letter.isdigit()]))
print(f"Unique symbols used: {unique_cont}")
result = ""
last_digit_index = current_digit_index = -1
for index in range(len(text)):
    if text[index].isdigit():
        current_digit_index = index
    if current_digit_index != last_digit_index:
        number_len = 1
        for j in range(index + 1, len(text), 1):
            if not text[j].isdigit():
                break
            number_len += 1
        num = int(text[index:number_len+index])
        txt = text[last_digit_index + 1:index]
        for v in range(num):
            result += txt
        current_digit_index = current_digit_index + number_len - 1
        last_digit_index = current_digit_index

print(result)



