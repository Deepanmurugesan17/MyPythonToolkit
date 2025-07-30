collaborations = [
    {"project_id": "P101", "researcher": "Alice", "department": "CSE", "co_authors": ["Bob", "Charlie"]},
    {"project_id": "P102", "researcher": "Bob", "department": "ECE", "co_authors": ["Alice"]},
    {"project_id": "P103", "researcher": "Charlie", "department": "CSE", "co_authors": ["Alice", "Bob"]},
    {"project_id": "P104", "researcher": "David", "department": "MECH", "co_authors": ["Eve"]},
    {"project_id": "P105", "researcher": "Eve", "department": "MECH", "co_authors": ["David", "Charlie"]},
    {"project_id": "P106", "researcher": "Frank", "department": "CSE", "co_authors": []},
    {"project_id": "P107", "researcher": "Charlie", "department": "CSE", "co_authors": ["Eve"]},
]

'''
Problem : 1
{
    "Alice": {
        "co_authors": {"Bob", "Charlie"},
        "departments_collaborated": {"CSE", "ECE"}
    },
    ...
}

Problem : 2
Top Collaborator: Charlie (4 collaborators)
Cross-Department Collaborators: ['Alice', 'Bob', 'Charlie', 'Eve']
Find the researcher with the highest number of unique collaborators.

Problem : 3
List all researchers who have collaborated with people outside their own department.
'''
result  = {}
for i in collaborations:
    prj_id = i["project_id"]
    researcher = i["researcher"]
    department = i["department"]
    coauthors = i["co_authors"]
    if researcher not in result:
        result[researcher] = {
            "co_authors" : set(coauthors),
            "departments_collaborated" : set()
        }
    elif researcher in result:
        result[researcher]["co_authors"].update(coauthors)
#print(result)

researcher_dept = {}

for i in collaborations:
    prj_id = i["project_id"]
    researcher = i["researcher"]
    department = i["department"]
    coauthors = i["co_authors"]
    if researcher not in researcher_dept:
        researcher_dept[researcher] = department
print("Researcher and Their Associated Departments were :")
print(researcher_dept)

for key, value in result.items():
    researcher = key
    coauthors = value["co_authors"]
    departments_collaborated = value["departments_collaborated"]
    for i in coauthors:
        if i in researcher_dept:
            result[researcher]["departments_collaborated"].add(researcher_dept[i])
print()
print(result)

max_count = 0
max_researcher = []
for key, values in result.items():
    name = key
    collaborators = len(values["co_authors"])
    if collaborators > max_count:
        max_count = collaborators
        max_researcher = [name]
    elif collaborators == max_count:
        max_researcher.append(collaborators)
print()
print(f"The Researcher with the highest number of unique collaborators is {' '.join(max_researcher)}")

result_1 = {}

for key,values in researcher_dept.items():
    researcher_name = key
    researcher_dept_name = values
    for i, j in result.items():
        name = i
        if researcher_name == i:
            for k in j["departments_collaborated"]:
                if (k != researcher_dept_name) and (researcher_name not in result_1):
                    result_1[researcher_name] = set([k])
                elif (k != researcher_dept_name) and (researcher_name in result_1):
                    result_1[researcher_name].add(k)
print("\nThe Researchers who have collaborated with people outside their own department were : ")
print(result_1)