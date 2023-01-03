price_mackerel = float(input())
price_sprinkle = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = float(input())

bonito_price = (price_mackerel + price_mackerel * 0.60) * bonito_kg
safrid_price = (price_sprinkle + price_sprinkle * 0.80) * safrid_kg
mussels_price = mussels_kg * 7.50
total_price = bonito_price + safrid_price + mussels_price
print(f'{total_price:.2f}')

