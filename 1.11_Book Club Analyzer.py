ratings = [
    ("Alice", "1984", 4),
    ("Bob", "1984", 5),
    ("Alice", "Brave New World", 5),
    ("Charlie", "1984", 3),
    ("Bob", "Brave New World", 4),
    ("Charlie", "Fahrenheit 451", 5),
    ("Alice", "Fahrenheit 451", 2),
    ("Bob", "Fahrenheit 451", 4),
    ("Charlie", "Brave New World", 4)
]

member_ratings = {}
'''
member_ratings = {
    'Alice': {'1984': 4, 'Brave New World': 5, 'Fahrenheit 451': 2},
    ...
}

'''
for i in ratings:
    name = i[0]
    book = i[1]
    rating = i[2]
    if name not in member_ratings:
        member_ratings[name] = {}
    if book not in member_ratings[name]:
        member_ratings[name][book] = rating
print(member_ratings)
print()
#Print the average rating each member has given across all books they've rated.
max_rating = 0
max_rating_name = set()
for key,values in member_ratings.items():
    name = key
    rating_count = 0
    rating_score = 0
    for book_name, score in values.items():
        rating_count += 1
        rating_score += score

    average_rating = round((rating_score / rating_count),2)
    if average_rating > max_rating:
        max_rating = average_rating
        max_rating_name = ([name])
    elif average_rating == max_rating:
        max_rating_name.add(name)
    print(f"Average Rating given by {name} across {rating_count} books is {average_rating}")
print()
book_ratings = {}
'''
{
    '1984': {'Alice': 4, 'Bob': 5, 'Charlie': 3},
    ...
}
'''
for i in ratings:
    name = i[0]
    book = i[1]
    rating = i[2]
    if book not in book_ratings:
        book_ratings[book] = {}
    if name not in book_ratings[book]:
        book_ratings[book][name] = rating
print(book_ratings)
print()
'''
For each book, print:
Average rating received

Name(s) of the member(s) who gave it the highest rating
'''
for key,values in book_ratings.items():
    book = key
    rating_count_book = 0
    rating_score_book = 0
    for person, score in values.items():
        rating_count_book += 1
        rating_score_book += score

    average_rating = round((rating_score_book / rating_count_book),2)
    print(f"Average Rating given for {book} by {rating_count_book} persons is {average_rating}")
print()
#(Bonus) Identify the most generous rater (i.e., member whose average rating given is the highest among all members).
print(f"The Most Generous rater is : {','.join(max_rating_name)} with rating score of {max_rating}")