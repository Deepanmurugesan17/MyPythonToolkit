people = [
    {"name": "Anita", "hobbies": ["Reading", "Traveling", "Music"]},
    {"name": "Ravi", "hobbies": ["Sports", "Music", "Cooking"]},
    {"name": "Suresh", "hobbies": ["Reading", "Music", "Photography"]},
    {"name": "Divya", "hobbies": ["Cooking", "Music", "Traveling"]}
]

result = {}

for i in people:
    name = i["name"]
    hobby = i["hobbies"]
    if name not in result:
        result[name] = hobby
    else:
        result[name].extend[hobby]

max_hobbies = {}

for key, values in result.items():
    name = key
    hobby = values
    hobby_count = len(values)
    print(f"{key} has {hobby_count} unique hobbies")
    for i in hobby:
        if i not in max_hobbies:
            max_hobbies[i] = 1
        else:
            max_hobbies[i] += 1
max_hobby_value = 0
max_hobby = []
for key, values in max_hobbies.items():
    if values > max_hobby_value:
        max_hobby_value = values
        max_hobby = [key]
    elif values == max_hobby_value:
        max_hobby.append(key)

print(f"Most common hobby: {','.join(max_hobby)} (liked by {max_hobby_value} people)")


