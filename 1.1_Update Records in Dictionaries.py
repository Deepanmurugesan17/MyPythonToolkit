records = [
    {"department": "CSE", "name": "Anita", "score": 85},
    {"department": "ECE", "name": "Ravi", "score": 78},
    {"department": "CSE", "name": "Suresh", "score": 92},
    {"department": "MECH", "name": "Divya", "score": 74},
    {"department": "CSE", "name": "Anita", "score": 90},
    {"department": "ECE", "name": "Ravi", "score": 82},
    {"department": "MECH", "name": "Suresh", "score": 70},
    {"department": "CSE", "name": "Divya", "score": 88},
]
result = {}
department = set()
for i in records:
    dept = i["department"]
    name = i["name"]
    marks = i["score"]
    department.add(dept)
    if dept not in result:
        result[dept] = {name : [marks]}
    elif dept in result and name not in result[dept]:
        result[dept][name] = [marks]
    elif dept in result and name in result[dept]:
        result[dept][name].append(marks)
#print(result)

for x in department:
    print(f"\n{x} : Department :")
    for key, value in result.items():
        dept = key
        if dept == x:
            for i, j in value.items():
                name = i
                marks = j
                total_marks = sum(marks)
                total_exams = len(marks)
                avg = round((total_marks / total_exams), 2)
                print(f"{name} : {avg}")