from math import sqrt


def get_primes(list_int):
    # for el in list_int:
    #     if el <= 1:
    #         continue
    #
    #     for divisor in range(2, el):
    #         if el % divisor == 0:
    #             break
    #
    #     else:
    #         yield el
    for el in list_int:
        if el <= 1:
            continue

        for divisor in range(2, int(sqrt(el)) + 1):
            if el % divisor == 0:
                break

        else:
            yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
