line = input()
dwarfs_dict = {}
colors_dict = {}
while line != "Once upon a time":
    tokens = line.split(" <:> ")
    name = tokens[0]
    color = tokens[1]
    physics = int(tokens[2])
    id = name + ":" + color
    if id not in dwarfs_dict:
        if color not in colors_dict:
            colors_dict[color] = 1
        else:
            colors_dict[color] += 1
        dwarfs_dict[id] = [0, color]
    dwarfs_dict[id][0] = max([dwarfs_dict[id][0], physics])
    line = input()

sorted_dwarfs = dict(sorted(dwarfs_dict.items(), key=lambda x: (x[1][0], colors_dict[x[1][1]]), reverse=True))
for key, value in sorted_dwarfs.items():
    tokens = key.split(":")
    print(f"({tokens[1]}) {tokens[0]} <-> {value[0]}")

# x се достъпва като двумерен масив: x[ id, [physics, color]]
# x[0] връща id-то
# x[1] ни дава достъп до елеметите на [physics, color]
# x[1][0] връща първия елемент, който в случая е physics
# x[1][1] връща втория елемент, който в случая е color
# С други думи, colors_dict[x[1][1]]  ще върне броя джуджета с цвета на джуджето, което се сортира в момента.