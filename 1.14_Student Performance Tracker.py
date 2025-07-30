records = [
    {"name": "Alice", "subject": "Math", "marks": 90},
    {"name": "Alice", "subject": "Math", "marks": 85},
    {"name": "Alice", "subject": "Science", "marks": 92},
    {"name": "Bob", "subject": "Math", "marks": 78},
    {"name": "Charlie", "subject": "Math", "marks": 65},
    {"name": "Charlie", "subject": "Math", "marks": 70},
    {"name": "Charlie", "subject": "Science", "marks": 80}
]
'''
{
    'Alice': {'Math': 87.5, 'Science': 92.0},
    'Bob': {'Math': 78.0},
    'Charlie': {'Math': 67.5, 'Science': 80.0}
}
'''
#subject_list= set(i["subject"] for i in records)
#print(subject_list)

result = {}


for i in records:
    name = i["name"]
    subject = i["subject"]
    marks = i["marks"]
    if name not in result:
        result[name] = {}
    if (name in result) and (subject not in result[name]):
        result[name][subject] = [marks]
    elif (name in result) and (subject in result[name]):
        result[name][subject].append(marks)
#print(result)

final_set = {}

for key,values in result.items():
    name = key
    for subject,marks in values.items():
        total_marks = sum(marks)
        total_exams_attempted = len(marks)
        avg_marks = round(total_marks/total_exams_attempted,2)
        if name not in final_set:
            final_set[name] = {}
        if subject not in final_set[name]:
            final_set[name][subject] = avg_marks
print("Average marks for each students and their associated subjects were : \n")
print(final_set)
