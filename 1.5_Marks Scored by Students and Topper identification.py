records = [
    {"name": "Anita", "subject": "Math", "marks": 85},
    {"name": "Ravi", "subject": "Math", "marks": 78},
    {"name": "Anita", "subject": "Science", "marks": 92},
    {"name": "Ravi", "subject": "Science", "marks": 88},
    {"name": "Anita", "subject": "English", "marks": 75},
    {"name": "Ravi", "subject": "English", "marks": 82},
    {"name": "Suresh", "subject": "Math", "marks": 80},
    {"name": "Suresh", "subject": "Science", "marks": 85},
    {"name": "Suresh", "subject": "English", "marks": 78},
]
result = {}

for i in records:
    name = i['name']
    subject = i['subject']
    marks = i['marks']
    if name not in result:
        result[name] = {
            "Subject": [subject],
            "Marks": [marks]
        }
    else:
        result[name]["Subject"].append(subject)
        result[name]["Marks"].append(marks)

top_score = 0
top_score_student = []

for key, values in result.items():
    subjects = ','.join(values['Subject'])
    total = sum(values['Marks'])

    print(f"{key} Scored {total} marks with enrolled subject such as {subjects}.")
    if total > top_score:
        top_score = total
        top_score_student = ([key])
    elif total == top_score:
        top_score_student.append(key)

print(f"Topper(s): {','.join(top_score_student)} with {top_score} marks.")
