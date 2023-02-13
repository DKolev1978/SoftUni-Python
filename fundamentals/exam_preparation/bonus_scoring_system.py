from math import ceil

number_of_the_students = int(input())
number_of_the_lectures = int(input())
additional_bonus = int(input())

max_attendance = 0
for _ in range(number_of_the_students):
    attendance_of_each_student = int(input())
    max_attendance = max(attendance_of_each_student, max_attendance)

total_bonus = 0
if number_of_the_lectures != 0:
    total_bonus = (max_attendance / number_of_the_lectures) * (5 + additional_bonus)

print(f"Max Bonus: {ceil(total_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")
