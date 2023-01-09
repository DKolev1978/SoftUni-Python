input_line = input()
dishes_count = 0
dishwasher_counter = 0
detergent_used = 0
flag = True
total_dishes = 0
total_pots = 0
total_detergent_used = 0
detergent = int(input_line) * 750
while detergent >= total_detergent_used:
    input_line = input()
    if input_line == "End":
        flag = False
        break
    else:
        dishes_count = int(input_line)
        dishwasher_counter += 1
        if dishwasher_counter == 3:
            dishwasher_counter = 0
            detergent_used = dishes_count * 15
            total_pots += dishes_count
        else:
            detergent_used = dishes_count * 5
            total_dishes += dishes_count
    total_detergent_used += detergent_used
diff = abs(detergent - total_detergent_used)
if flag:
    print(f"Not enough detergent, {diff} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{total_dishes} dishes and {total_pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")



