n = input()

presentations_counter = 0
total_average_marks = 0
average_marks = 0
flag = False

while n != "Finish":
    presentation_name = input()
    if presentation_name == "Finish":
        flag = True
        break

    marks_int = int(n)
    average_mark = 0
    total_marks = 0

    for i in range(marks_int):
        marks = input()
        total_marks += float(marks)
        average_mark = total_marks / marks_int

    print(f'{presentation_name} - {average_mark:.2f}.')
    presentations_counter += 1
    total_average_marks += average_mark
    average_marks = total_average_marks / presentations_counter


print(f"Student's final assessment is {average_marks:.2f}.")