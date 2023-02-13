def get_chr_in_range(start, end):
    result = ''
    for num in range(ord(start) + 1, ord(end)):
        result += f'{chr(num)} '
    return result


start_char = input()
end_char = input()
print(get_chr_in_range(start_char, end_char))