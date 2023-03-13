employee_id_by_company = {}

while True:
    user_input = input()
    if user_input == "End":
        break

    company_name, employee_id = user_input.split(" -> ")
    if company_name not in employee_id_by_company:
        employee_id_by_company[company_name] = []

    if employee_id not in employee_id_by_company[company_name]:
        employee_id_by_company[company_name].append(employee_id)
    else:
        continue

for company_name, employee_id in employee_id_by_company.items():
    print(company_name)
    for id in employee_id_by_company[company_name]:
        print(f"-- {id}")
