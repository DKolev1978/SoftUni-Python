price_vegetables = float(input())
price_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

total_price_fruits = kg_fruits * price_fruits
total_price_vegetables = kg_vegetables * price_vegetables
total_price = (total_price_vegetables + total_price_fruits) / 1.94
print(f'{total_price:.2f}')


