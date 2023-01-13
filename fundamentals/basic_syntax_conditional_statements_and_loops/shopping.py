budget = int(input())
user_input = input()
while user_input != "End":
    user_input = int(user_input)
    budget -= user_input

    if budget < 0:
        print("You went in overdraft!")
        break
    user_input = input()
else:
    print("You bought everything needed.")
