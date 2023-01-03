corner_symbol = '+ '
side_symbol = '| '
center_symbol = '- '

lines = int(input())

print(corner_symbol + (lines - 2) * center_symbol + corner_symbol)

for line in range(1, lines - 1):
    print(side_symbol + (lines - 2) * center_symbol + side_symbol)

print(corner_symbol + (lines - 2) * center_symbol + corner_symbol)