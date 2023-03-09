countries = [country for country in input().split(", ")]
capitals = [capital for capital in input().split(", ")]

capitals_by_country = dict.fromkeys(countries)
i = 0
for country in countries:
    capitals_by_country[country] = capitals[i]
    i += 1

for country, capital in capitals_by_country.items():
    print(f"{country} -> {capital}")