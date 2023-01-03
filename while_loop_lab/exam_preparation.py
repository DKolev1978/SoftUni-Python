task_to_failed = int(input())

task_failed = 0
task_solved = 0
marks_sum = 0
last_task = ''
has_failed = True

while task_failed < task_to_failed:
    task_name = input()
    if task_name == "Enough":
        has_failed = False
        break

    mark = int(input())
    if mark <= 4:
        task_failed += 1
    task_solved += 1
    marks_sum += mark
    last_task = task_name

if has_failed:
    print(f"You need a break, {task_failed} poor grades.")
else:
    print(f"Average score: {marks_sum / task_solved:.2f}")
    print(f"Number of problems: {task_solved}")
    print(f"Last problem: {last_task}")

