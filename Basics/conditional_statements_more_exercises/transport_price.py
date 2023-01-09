n = int(input())
input_line = input()

taxi_day_price = 0.70 + n * 0.79
taxi_night_price = 0.70 + n * 0.90
autobus_price = 0.09 * n
train_price = 0.06 * n

if n < 20:
    if input_line == 'day':
        print(f'{taxi_day_price:.2f}')
    else:
        print(f'{taxi_night_price:.2f}')

elif 20 <= n < 100:
    print(f'{autobus_price:.2f}')
elif n >= 100:
    print(f'{train_price:.2f}')




