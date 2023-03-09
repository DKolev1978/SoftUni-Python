courses_by_student_id = {}

user_input = input()
while ":" in user_input:
    name, student_id, course = user_input.split(":")
    if course not in courses_by_student_id:
        courses_by_student_id[course] = {student_id: name}
    else:
        courses_by_student_id[course][student_id] = name

    user_input = input()
course_name = user_input.replace("_", " ")
students = courses_by_student_id[course_name]

for st_id, name in students.items():
    print(f"{name} - {st_id}")



