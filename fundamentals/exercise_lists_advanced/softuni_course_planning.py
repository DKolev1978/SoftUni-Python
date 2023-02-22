lessons = input().split(", ")

while True:
    input_line = input()
    if input_line == "course start":
        break
    command_seq = input_line.split(":")
    command = command_seq[0]
    lesson_title = command_seq[1]
    if command == "Add":
        if lesson_title not in lessons:
            lessons.append(lesson_title)
    elif command == "Insert":
        index = int(command_seq[2])
        if lesson_title not in lessons:
            lessons.insert(index, lesson_title)
    elif command == "Remove":
        if lesson_title in lessons:
            lessons.remove(lesson_title)
    elif command == "Swap":
        current_title1 = command_seq[1]
        current_title2 = command_seq[2]
        if current_title1 in lessons and current_title2 in lessons:
            first_title = lessons.index(current_title1)
            second_title = lessons.index(current_title2)
            lessons[first_title], lessons[second_title] = lessons[second_title], lessons[first_title]

            first_exercise = f"{current_title1}-Exercise"
            second_exercise = f"{current_title2}-Exercise"

            if first_exercise in lessons and second_exercise not in lessons:
                lessons.remove(first_exercise)
                lessons.insert(lessons.index(current_title1) + 1, first_exercise)
            elif first_exercise not in lessons and second_exercise in lessons:
                lessons.remove(second_exercise)
                lessons.insert(lessons.index(current_title2) + 1, second_exercise)
            elif first_exercise in lessons and second_exercise in lessons:
                first = lessons.index(first_exercise)
                second = lessons.index(second_exercise)
                lessons[second], lessons[first] = lessons[first], lessons[second]
    elif command == "Exercise":
        if lesson_title in lessons and f"{lesson_title}-Exercise" not in lessons:
            needed_title_index = lessons.index(lesson_title)
            lessons.insert(needed_title_index + 1, f"{lesson_title}-Exercise")
        elif lesson_title not in lessons:
            lessons.append(lesson_title)
            lessons.append(f"{lesson_title}-Exercise")

for element in lessons:
    print(f"{lessons.index(element) + 1}.{element}")
