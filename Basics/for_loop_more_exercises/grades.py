students_count = int(input())
top_counter = 0
god_counter = 0
average_counter = 0
fail_counter = 0
total_grades = 0
for i in range(students_count):
    grade = float(input())
    if 5.00 <= grade:
        top_counter += 1
        total_grades += grade
    elif 4.00 <= grade < 5:
        god_counter += 1
        total_grades += grade
    elif 3.00 <= grade < 4:
        average_counter += 1
        total_grades += grade
    else:
        fail_counter += 1
        total_grades += grade
prc_top = top_counter / students_count * 100
prc_god = god_counter / students_count * 100
prc_average = average_counter / students_count * 100
prc_fail = fail_counter / students_count * 100
average_score = total_grades / students_count
print(f"Top students: {prc_top:.2f}%")
print(f"Between 4.00 and 4.99: {prc_god:.2f}%")
print(f"Between 3.00 and 3.99: {prc_average:.2f}%")
print(f"Fail: {prc_fail:.2f}%")
print(f"Average: {average_score:.2f}")