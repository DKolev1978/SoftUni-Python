import operator
from operator import itemgetter

color_by_name_points = {}
user_points_color = {}
line = input()
while line != "Once upon a time":
    name, colour, points = line.split(" <:> ")
    points = int(points)
    if colour not in color_by_name_points:
        color_by_name_points[colour] = {}
    if name not in color_by_name_points[colour]:
        color_by_name_points[colour][name] = points
    elif points > color_by_name_points[colour][name]:
        color_by_name_points[colour][name] = points

    if name not in user_points_color:
        user_points_color[name] = {}
    if colour not in user_points_color[name]:
        user_points_color[name][points] = colour
    elif points > user_points_color[name][colour]:
        user_points_color[name][colour] = points

    line = input()

r = [(C,K,n) for C,d in color_by_name_points.items() for K,n in d.items()]
r.sort(key=lambda ckn:ckn[-1], reverse=True)
first_value = list(color_by_name_points.values())[0]
if not list(color_by_name_points.values()).count(first_value) == len(color_by_name_points):
    color_by_name_points_ordered = dict(sorted(color_by_name_points.items(), key=lambda kv: (len(kv[1]), kv[0]), reverse=True))
    for key, value in color_by_name_points_ordered.items():
        print(f"({key}) ", end="")
        for k, v in value.items():
            print(f"{k} <:> {v}")
else:
    for C,K,n in r: print(f"({C}) {K} <-> {n}")



