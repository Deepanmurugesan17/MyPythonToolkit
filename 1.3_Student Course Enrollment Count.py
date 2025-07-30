submissions = [
    {"student": "Anita", "subject": "Math"},
    {"student": "Ravi", "subject": "Science"},
    {"student": "Anita", "subject": "Science"},
    {"student": "Ravi", "subject": "Math"},
    {"student": "Suresh", "subject": "Math"},
    {"student": "Anita", "subject": "Math"},  # duplicate for testing
    {"student": "Ravi", "subject": "Science"},
    {"student": "Suresh", "subject": "Science"},
    {"student": "Anita", "subject": "English"},
    {"student": "Suresh", "subject": "Science"}  # another duplicate
]

# Most active student(s): Anita (4 submissions)
result = {}
for i in submissions:
    stud_name = i['student']
    assignment = i['subject']

    if stud_name not in result:
        result[stud_name] = set([assignment])
    else:
        result[stud_name].add(assignment)

for key, value in result.items():
    print(f"{key} has enrolled {len(value)} Courses")
