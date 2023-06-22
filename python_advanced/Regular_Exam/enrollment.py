def gather_credits(credits, *args):
    cources_enrowed = []
    max_credits = 0
    print()
    for course, credit in args:
        if course in cources_enrowed:
            continue
        cources_enrowed.append(course)
        credits -= int(credit)
        max_credits += int(credit)
        if credits < 0:
            return f"Enrollment finished! Maximum credits: {max_credits}.\n" \
                   f"Courses: {', '.join(sorted(cources_enrowed))}"

    if credits > 0:
        return f"You need to enroll in more courses! You have to gather {credits} credits more."
    else:
        return f"Enrollment finished! Maximum credits: {max_credits}.\n" \
               f"Courses: {', '.join(sorted(cources_enrowed))}"


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

from unittest import TestCase, main


class Test(TestCase):
    def test_students_credits(self):
        result = gather_credits(
            60,
            ("Basics", 27),
            ("Fundamentals", 27),
            ("Advanced", 30),
            ("Web", 30)

        )

        self.assertEqual(
            result.strip(),
            """Enrollment finished! Maximum credits: 84.
Courses: Advanced, Basics, Fundamentals""")


if __name__ == '__main__':
    main()


