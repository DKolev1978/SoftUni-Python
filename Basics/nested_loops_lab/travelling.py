destination = input ()
all_money_saved = 0

while destination != "End":
    budget = float(input())
    while True:
        money_saved = float(input())
        all_money_saved += money_saved
        if all_money_saved >= budget:
            print(f"Going to {destination}!")
            all_money_saved = 0
            break
    destination = input()
