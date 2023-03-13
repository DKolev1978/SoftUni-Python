students_by_courses = {}
while True:
    command = input()
    if command == "end":
        break

    course, student_name = command.split(" : ")
    if course not in students_by_courses:
        students_by_courses[course] = []
    students_by_courses[course].append(student_name)

for course, names in students_by_courses.items():
    print(f"{course}: {len(students_by_courses[course])}")
    for name in names:
        print(f"-- {name}")