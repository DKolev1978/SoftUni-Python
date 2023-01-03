fuel_type = input()
litters_fuel = float(input())
club_card = input()

gasoline_price = 2.22 * litters_fuel
diesel_price = 2.33 * litters_fuel
gas_price = 2.33 * litters_fuel

if club_card == 'Yes':
    gas_price = (0.93 - 0.08) * litters_fuel
    gasoline_price = (2.22 - 0.18) * litters_fuel
    diesel_price = (2.33 - 0.12) * litters_fuel
    if 20 <= litters_fuel <= 25:
        if fuel_type == 'Gas':
            gas_price = gas_price - gas_price * 0.08
            print(f"{gas_price:.2f} lv.")
        elif fuel_type == 'Gasoline':
            gasoline_price = gasoline_price - gasoline_price * 0.08
            print(f"{gasoline_price:.2f} lv.")
        elif fuel_type == 'Diesel':
            diesel_price = diesel_price - diesel_price * 0.08
            print(f"{diesel_price:.2f} lv.")
    elif litters_fuel > 25:
        if fuel_type == 'Gas':
            gas_price = gas_price - gas_price * 0.10
            print(f"{gas_price:.2f} lv.")
        elif fuel_type == 'Gasoline':
            gasoline_price = gasoline_price - gasoline_price * 0.10
            print(f"{gasoline_price:.2f} lv.")
        elif fuel_type == 'Diesel':
            diesel_price = diesel_price - diesel_price * 0.10
            print(f"{diesel_price:.2f} lv.")
    elif litters_fuel < 20:
        if fuel_type == 'Gas':
            print(f"{gas_price:.2f} lv.")
        elif fuel_type == 'Gasoline':
            print(f"{gasoline_price:.2f} lv.")
        elif fuel_type == 'Diesel':
            print(f"{diesel_price:.2f} lv.")

elif club_card == 'No':
    gas_price = 0.93 * litters_fuel
    gasoline_price = 2.22 * litters_fuel
    diesel_price = 2.33 * litters_fuel
    if 20 <= litters_fuel <= 25:
        if fuel_type == 'Gas':
            gas_price = gas_price - gas_price * 0.08
            print(f"{gas_price:.2f} lv.")
        elif fuel_type == 'Gasoline':
            gasoline_price = gasoline_price - gasoline_price * 0.08
            print(f"{gasoline_price:.2f} lv.")
        elif fuel_type == 'Diesel':
            diesel_price = diesel_price - diesel_price * 0.08
            print(f"{diesel_price:.2f} lv.")
    elif litters_fuel > 25:
        if fuel_type == 'Gas':
            gas_price = gas_price - gas_price * 0.10
            print(f"{gas_price:.2f} lv.")
        elif fuel_type == 'Gasoline':
            gasoline_price = gasoline_price - gasoline_price * 0.10
            print(f"{gasoline_price:.2f} lv.")
        elif fuel_type == 'Diesel':
            diesel_price = diesel_price - diesel_price * 0.10
            print(f"{diesel_price:.2f} lv.")
    elif litters_fuel < 20:
        if fuel_type == 'Gas':
            print(f"{gas_price:.2f} lv.")
        elif fuel_type == 'Gasoline':
            print(f"{gasoline_price:.2f} lv." )
        elif fuel_type == 'Diesel':
            print(f"{diesel_price:.2f} lv.")






