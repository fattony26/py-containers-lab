# Exercise 1
students = ['jojo', 'abdel', 'lara', 'mike', 'jay', 'mario']
print(students[1])
print(students[-1])


# Exercise 2
foods = ('spaghetti', 'ramen', 'salad', 'turkey leg', 'MRE', 'french toast')

for food in foods:
    print(f'{food} is a good food')


# Exercise 3
for food in foods[-2:]:
    print(food)

# Exercise 4
home_town = {
    'city': 'Arlington',
    'state': 'VA',
    'population': 'Over 9000'
}
print(f'I was born in {home_town["city"]} {home_town["state"]} - population {home_town["population"]}')


# Exercise 5
for k, v in home_town.items():
    print(f'{k}: {v}')


# Exercise 6
cohort = []
for i, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[i]
    })
for student in cohort:
    print(cohort)


# Exercise 7
awesome_students = []
for student in students:
    awesome_students.append(f"{student} is awesome!")
for student in awesome_students:
    print(student)


# Exercise 8
for food in foods:
    if 'a' in food:
        print(food)