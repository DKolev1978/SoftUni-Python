capacity_of_the_stadium = int(input())
fan_count = int(input())
a_counter = 0
b_counter = 0
v_counter = 0
g_counter = 0


for i in range(fan_count):
    sector = input()
    if sector == "A":
        a_counter += 1
    elif sector == "B":
        b_counter += 1
    elif sector == "V":
        v_counter += 1
    elif sector == "G":
        g_counter += 1

print(f"{a_counter / fan_count * 100:.2f}%")
print(f"{b_counter / fan_count * 100:.2f}%")
print(f"{v_counter / fan_count * 100:.2f}%")
print(f"{g_counter / fan_count * 100:.2f}%")
print(f"{fan_count / capacity_of_the_stadium * 100:.2f}%")