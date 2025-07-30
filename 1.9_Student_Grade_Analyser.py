marks = [
    ("Alice", "Math", 85),
    ("Bob", "Math", 78),
    ("Alice", "English", 92),
    ("Bob", "English", 81),
    ("Alice", "Science", 74),
    ("Bob", "Science", 69),
    ("Alice", "Math", 5),       # Bonus marks
    ("Bob", "English", 4),      # Bonus marks
    ("Alice", "Science", 1)     # Bonus marks
]

'''
{
    'Alice': {'Math': total, 'English': total, ...},
    'Bob': {'Math': total, 'English': total, ...}
}

'''

result = {}

for i in marks:
    name = i[0]
    subject = i[1]
    marks = i[2]
    if name not in result:
        result[name] = {}
    if subject not in result[name]:
        result[name][subject] = marks
    else:
        result[name][subject] += marks
print(result)

#To find the total marks scored by each student
#To Find the Top Scoring subject by a student

for key,values in result.items():
    name = key
    marks = values
    total_marks = 0
    max_marks = 0
    subject = []
    for x,y in marks.items():
        if y > max_marks:
            max_marks = y
            subject = [x]
        elif y == max_marks:
            subject.append(x)
        total_marks += y
    print(f"{name} has scored {total_marks}")
    print(f"Top Scored Subject by {name} is {','.join(subject)} and associated mark is {max_marks}")
