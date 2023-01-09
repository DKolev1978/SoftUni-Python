from math import ceil

n = int( input() )

limit = (n - 1) // 2

if n % 2 != 0:
    number_of_stars = 1
    number_of_dashes = limit
    for line in range(0, limit):
        print("-" * number_of_dashes + "*" * number_of_stars + "-" * number_of_dashes)
        number_of_stars += 2
        number_of_dashes -= 1

else:
    number_of_stars = 2
    number_of_dashes = limit
    for line in range(0, limit):
        print("-" * number_of_dashes + "*" * number_of_stars + "-" * number_of_dashes)
        number_of_stars += 2
        number_of_dashes -= 1

for line in range( 1, n + 1 ):
    if line == ceil( n / 2 ):
        print("*" * n )

for line in range( 0, n // 2 ):
    print("|" + "*" * (n - 2) + "|")