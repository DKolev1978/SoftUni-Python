n = int(input())

presentations_counter = 0
total_average_marks = 0
average_marks = 0
flag = False
input_line = input()
while input_line != "Finish":
    presentation_name = input_line

    total_marks = 0

    for i in range(n):
        marks = float(input())
        total_marks += marks
        average_mark = total_marks / n

    print(f'{presentation_name} - {average_mark:.2f}.')
    presentations_counter += 1
    total_average_marks += average_mark
    average_marks = total_average_marks / presentations_counter
    input_line = input()


print(f"Student's final assessment is {average_marks:.2f}.")