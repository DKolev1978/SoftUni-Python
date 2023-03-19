number_rows = int(input())
grades_by_student = {}

for _ in range(number_rows):
    student_name = input()
    grade = float(input())
    if student_name not in grades_by_student:
        grades_by_student[student_name] = []
    grades_by_student[student_name].append(grade)

for student_name, grade in grades_by_student.items():
    average_grade = sum(grades_by_student[student_name]) / len(grades_by_student[student_name])
    if average_grade >= 4.50:
        print(f"{student_name} -> {average_grade:.2f}")