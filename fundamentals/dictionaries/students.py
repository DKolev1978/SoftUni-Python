data = input()
dick = {}

while ":" in data:
    name, id, cource = data.split(":")

    if cource not in dick:
        dick[cource] = {id: name}
    else:
        dick[cource][id] = name
    data = input()

course_name = data.replace("_", " ")
students = dick[course_name]

for st_id, name in students.items():
    print(f"{name} - {st_id}")
