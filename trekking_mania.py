group_count = int(input())
musala_count = 0
monblan_count = 0
kilim_count = 0
ktwo_count = 0
everest_count = 0
total_people = 0

for i in range(1, group_count + 1):
    count_people = int(input())
    if count_people <= 5:
        musala_count += count_people
    elif count_people <= 12:
        monblan_count += count_people
    elif count_people <= 25:
        kilim_count += count_people
    elif count_people <= 40:
        ktwo_count += count_people
    else:
        everest_count += count_people

total_people = musala_count + monblan_count + kilim_count + ktwo_count + everest_count
print(f'{(musala_count / total_people) * 100:.2f}%')
print(f'{(monblan_count / total_people) * 100:.2f}%')
print(f'{(kilim_count / total_people) * 100:.2f}%')
print(f'{(ktwo_count / total_people) * 100:.2f}%')
print(f'{(everest_count / total_people) * 100:.2f}%')



