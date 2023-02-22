def replace_str(elements):
    x = list(elements)
    temp = x[1]
    x[1] = x[-1]
    x[-1] = temp
    return "".join(x)


secret_message = input().split()
digits = ''
decipher = []
decipher_new = []

for element in secret_message:
    counter = 0
    for idx in range(len(element)):
        if element[idx].isdigit():
            digits += element[idx]
            counter += 1
        else:
            continue
    element = element[counter:]
    element = chr(int(digits)) + element
    decipher.append(element)
    digits = ''

for el in decipher:
    new_word = replace_str(el)
    decipher_new.append(new_word)


print(' '.join([str(word) for word in decipher_new]))



