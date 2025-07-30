core_subjects = {"Math", "Science", "English"}

submissions = [
    {"student": "Anita", "subject": "Math"},
    {"student": "Ravi", "subject": "Science"},
    {"student": "Anita", "subject": "Science"},
    {"student": "Ravi", "subject": "Math"},
    {"student": "Suresh", "subject": "Math"},
    {"student": "Anita", "subject": "English"},
    {"student": "Ravi", "subject": "Science"},
    {"student": "Suresh", "subject": "Science"},
    {"student": "Suresh", "subject": "English"},
    {"student": "Ravi", "subject": "English"}
]
result = {}

for i in submissions:
    stud_name = i['student']
    assignment = i['subject']

    if stud_name not in result and assignment in core_subjects:
        result[stud_name] = set([assignment])
    elif stud_name in result and assignment in core_subjects:
        result[stud_name].add(assignment)
# print(result)

for x, y in result.items():
    enrolled_count = len(y)
    if enrolled_count == len(core_subjects):
        print(f"{x} has enrolled for all {enrolled_count} core subjects and Courses name were {','.join(y)}")
    else:
        print(f"{x} has enrolled for only {enrolled_count} core subjects and Courses name were {','.join(y)}")
