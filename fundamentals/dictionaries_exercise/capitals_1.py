capitals_by_country = {}
countries = input().split(", ")
capitals = input().split(", ")
i = 0

for element in countries:
    capitals_by_country[element] = capitals[i]
    i += 1

for country, capital in capitals_by_country.items():
    print(f"{country} -> {capital}")
