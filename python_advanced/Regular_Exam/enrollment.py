def gather_credits(credits_required: int, *courses):
    full_list = {}

    for argument in courses:
        taken_course, received_credits = argument
        if sum(full_list.values()) < credits_required:
            if taken_course in full_list.keys():
                continue
            else:
                full_list[taken_course] = int(received_credits)
                if sum(full_list.values()) >= credits_required:
                    break
        else:
            break

    if sum(full_list.values()) >= credits_required:
        return f"Enrollment finished! Maximum credits: {sum(full_list.values())}.\nCourses: {', '.join(sorted(list(full_list.keys())))}"
    else:
        return f"You need to enroll in more courses! You have to gather {credits_required - sum(full_list.values())} credits more."