count_of_non_working_days = int(input())

count_of_working_days = 365 - count_of_non_working_days
tom_play_time = 30000
tom_total_play_time = count_of_working_days * 63 + count_of_non_working_days * 127
diff = abs(tom_play_time - tom_total_play_time)
diff_hours = diff // 60
diff_minutes = diff % 60

if diff_minutes < 10:
    if tom_play_time > tom_total_play_time:
        print('Tom will run away')
        print(f'{diff_hours} hours and 0{diff_minutes} minutes more for play')
    else:
        print('Tom sleeps well')
        print(f'{diff_hours} hours and 0{diff_minutes} minutes less for play')
else:
    if tom_play_time <= tom_total_play_time:
        print('Tom will run away')
        print(f'{diff_hours} hours and {diff_minutes} minutes more for play')
    else:
        print('Tom sleeps well')
        print(f'{diff_hours} hours and {diff_minutes} minutes less for play')


