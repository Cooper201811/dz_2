import csv


mydict = [
{'name': 'Mary', 'age': 25, 'job': 'Scientist'},
{'name': 'Mike', 'age': 8, 'job': 'CEO'},
{'name': 'John', 'age': 48, 'job': 'Teacher'}
]

with open('users.csv', 'w', encoding='utf-8') as f:

    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in mydict:
        writer.writerow(user)