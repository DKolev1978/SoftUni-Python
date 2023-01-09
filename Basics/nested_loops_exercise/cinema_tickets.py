input_line = input()

flag = False
total_standard_counter = 0
total_kid_counter = 0
total_student_counter = 0

while input_line != "Finish":
    movie_name = input_line
    free_seats = int(input())
    current_movie_count = 0
    standard_counter = 0
    kid_counter = 0
    student_counter = 0
    line = input()
    while line != "End":
        type_ticket = line
        current_movie_count += 1

        if type_ticket == "standard":
            student_counter += 1
            total_standard_counter += 1
        elif type_ticket == "kid":
            kid_counter += 1
            total_kid_counter += 1
        elif type_ticket == "student":
            standard_counter += 1
            total_student_counter += 1
        if current_movie_count >= free_seats:
            flag = True
            break

        line = input()
    percentage_cuuren_movie = current_movie_count / free_seats * 100
    print(f"{movie_name} - {percentage_cuuren_movie:.2f}% full.")

    input_line = input()
total_ticket = total_student_counter + total_kid_counter + total_standard_counter
print(f"Total tickets: {total_ticket}")
print(f"{total_student_counter / total_ticket * 100:.2f}% student tickets.")
print(f"{total_standard_counter / total_ticket * 100:.2f}% standard tickets.")
print(f"{total_kid_counter / total_ticket * 100:.2f}% kids tickets.")
