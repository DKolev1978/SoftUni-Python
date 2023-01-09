first_couple = int(input())
second_couple = int(input())
difference_first_couple = int(input())
difference_second_couple = int(input())

for num1 in range(first_couple, first_couple + difference_first_couple + 1):
    if num1 > 1:
        for i in range(2, num1):
            if (num1 % i) == 0:
                break
        else:
            for num2 in range(second_couple, second_couple + difference_second_couple + 1):
                if num2 > 1:
                    for j in range(2, num2):
                        if (num2 % j) == 0:
                            break
                    else:
                        print(f"{num1}{num2}")








