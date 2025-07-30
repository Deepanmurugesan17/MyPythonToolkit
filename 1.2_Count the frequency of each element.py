items = ["apple", "banana", "apple", "orange", "banana", "apple", "banana"]
'''
Count the frequency of each element.
Identify the element(s) that occur the most times.
Print:
The element(s)
Their count
'''

count = 0
items_1 = {}

for i in items:
    if i not in items_1:
        items_1[i] = 1
    else :
        items_1[i] += 1
print(items_1)

maxcount = 0
max_fruit_name = []

for x,y in items_1.items():
    if y > maxcount:
        maxcount = y
        max_fruit_name=[x]
    elif y == maxcount:
        max_fruit_name.append(x)
print(f"The Most Occured words were {' and '.join(max_fruit_name)} and its occurences were {maxcount}")
