sequence_integers = [int(x) for x in input().split()]
result = 0

while sequence_integers:
    index = int(input())
    num = 0
    if 0 <= index < len(sequence_integers):
        num = sequence_integers.pop(index)
    elif 0 > index:
        num_to_add = sequence_integers[-1]
        num = sequence_integers[0]
    else:
        num_to_add = sequence_integers[0]
        num = sequence_integers[-1]
        sequence_integers[-1] = sequence_integers[0]
    result += num
    for idx in range(len(sequence_integers)):
        if sequence_integers[idx] <= num:
            sequence_integers[idx] += num
        else:
            sequence_integers[idx] -= num

print(result)




