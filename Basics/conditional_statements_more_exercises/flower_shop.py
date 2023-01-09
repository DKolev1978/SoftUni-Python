from math import floor, ceil
count_magnolias = int(input())
count_hyacinths = int(input())
count_roses = int(input())
count_cacti = int(input())
gift_price = float(input())

total_price = count_magnolias * 3.25 + count_hyacinths * 4 + count_roses * 3.50 + count_cacti * 8
total_price_after_taxes = total_price - total_price * 0.05

diff = abs(total_price_after_taxes - gift_price)

if total_price_after_taxes >= gift_price:
    print(f'She is left with {floor(diff)} leva.')
else:
    print(f'She will have to borrow {ceil(diff)} leva.')
