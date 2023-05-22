# solution 1 - with matrix
num = int(input())
matrix = [[int(n) for n in input().split()] for row in range(num)]

primary_sum = 0
secondary_sum = 0

for i in range(num):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][num - i - 1]

print(abs(primary_sum - secondary_sum))


# solution 2 - without matrix; one loop less;
num = int(input())

primary_sum = 0
secondary_sum = 0

for row in range(num):
    line = [int(x) for x in input().split()]

    primary_sum += line[row]
    secondary_sum += line[num - row - 1]

print(abs(primary_sum - secondary_sum))