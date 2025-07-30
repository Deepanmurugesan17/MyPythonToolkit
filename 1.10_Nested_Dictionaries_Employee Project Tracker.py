data = [
    ("E001", "Alpha", 10),
    ("E002", "Alpha", 8),
    ("E001", "Beta", 5),
    ("E003", "Alpha", 12),
    ("E002", "Beta", 7),
    ("E003", "Beta", 9),
    ("E001", "Alpha", 2),   # extra hours
    ("E002", "Alpha", 4),   # extra hours
    ("E003", "Gamma", 15)
]
result = {}
project_hours = {}

for i in data:
    emp_id = i[0]
    project_name = i[1]
    hours = i[2]
    if emp_id not in result:
        result[emp_id] = {}
    if project_name not in result[emp_id]:
        result[emp_id][project_name] = hours
    else:
        result[emp_id][project_name] += hours
print(result)

#1.To Find The Total Work Hours done by an employee
#2.To Find the Maximum work hours done by an employee for an particular project
for key,values in result.items():
    emp_id = key
    details = values
    total_working_hours = 0
    max_hours = 0
    max_project = []
    for x,y in details.items():
        if y > max_hours:
            max_hours = y
            max_project = [x]
        elif y == max_hours:
            max_project.append(x)
        total_working_hours += y
        if x not in project_hours:
            project_hours[x] = y
        else:
            project_hours[x] += y
    print(f"{emp_id}:{total_working_hours}")
    print(f"Maximum Hours worked by {emp_id} were {','.join(max_project)} : {max_hours}")

# To Find The MAX hours worked in a project
max_project = []
max_project_hours = 0
for x,y in project_hours.items():
    project_names = x
    hours_worked = y
    if y > max_project_hours:
        max_project_hours = y
        max_project = x

print(f"Maximum hours worked by a employees for a project is {''.join(max_project)} and total Hours were {max_project_hours}")