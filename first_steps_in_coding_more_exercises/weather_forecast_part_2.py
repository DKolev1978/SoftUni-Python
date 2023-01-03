input_degrees = float(input())

if 26 <= input_degrees <= 35:
    print('Hot')
elif 20.1 <= input_degrees <= 25.9:
    print('Warm')
elif 15.00 <= input_degrees <= 20.00:
    print('Mild')
elif 12.00 <= input_degrees <= 14.9:
    print("Cool")
elif 5.00 <= input_degrees <= 11.9:
    print('Cold')
else:
    print('unknown')