calculation_count_days = int(input())
doctors_count = 7
treated_patients_count = 0
untreated_patients_count = 0
days_counter = 0

for days in range(1, calculation_count_days + 1):
    days_counter += 1
    if days_counter % 3 == 0 and untreated_patients_count > treated_patients_count:
        doctors_count += 1
    patients = int(input())
    if doctors_count >= patients:
        treated_patients_count += patients
    else:
        treated_patients_count += doctors_count
        untreated_patients_count += patients - doctors_count

print(f"Treated patients: {treated_patients_count}.")
print(f"Untreated patients: {untreated_patients_count}.")

