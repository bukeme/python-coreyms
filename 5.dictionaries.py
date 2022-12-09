student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 1: 'Figure'}

print(student)
print(student['courses'])
print(student[1])
print(student.get('name')) # doesn't throw an error
print(student.get('grade'))
print(student.get('grade', 'Not Found'))

# student['phone'] = '555-555-555'
# student['name'] = 'Jane'

student.update({'name': 'Jane', 'age': 26, 'phone': '555'})
print(student)

# del student['age']
# print(student)

# age = student.pop('age')
# print(student)
# print(age)
# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
