# You will be receiving names of students, their ID, and a course of programming they have taken in the format
# "{name}:{ID}:{course}". On the last line, you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding
# course in the format: "{name} - {ID}" on separate lines.

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
