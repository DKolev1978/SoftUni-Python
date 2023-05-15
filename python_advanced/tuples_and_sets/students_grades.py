from collections import defaultdict


number_of_students = int(input())
grades_by_student = defaultdict(lambda: [])

for _ in range(number_of_students):
    student, grade = tuple(input().split())
    grade = float(grade)
    grades_by_student[student].append(grade)

for student, grades in grades_by_student.items():
    avg = sum(grades) / len(grades)
    print(f"{student} -> {' '.join([str(f'{grade:.2f}')for grade in grades])} (avg: {avg:.2f})")
