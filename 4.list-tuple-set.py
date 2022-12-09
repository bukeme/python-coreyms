courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))
print(courses[1])
print(courses[-1])
# Slicing
print(courses[0:2])
print(courses[:2])
print(courses[2:])

courses.append('Art')
print(courses)

courses.insert(0, 'Art')
print(courses)
courses_2 = ['Social Science', 'Education']
# courses.insert(0, courses_2)
courses.extend(courses_2)
print(courses)
courses.remove('Math')
print(courses)
popped = courses.pop()
print(courses)
print(popped)

# courses.reverse()
# print(courses)

# courses.sort()
# print(courses)

nums = [1, 5, 4, 3, 2]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
sorted_courses = sorted(courses)
# print(courses)
# print(sorted_courses)
# print(min(nums))
# print(max(nums))
# print(sum(nums))

# print(courses.index('CompSci'))
# print('Art' in courses)
# print('Engineering' in courses)

# for item in courses:
#     print(item)

# for index, course in enumerate(courses, start=1):
#     print(index, course)

# course_str = '-'.join(courses)
# print(course_str)
# new_list = course_str.split('-')
# print(new_list)

# Tuples(are immutable)
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)

# Set
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Art', 'Design', 'CompSci'}
print(cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

#Empty Lists
empty_list = []
empty_list = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets
empty_set = {} # This is wrong!. It's an empty dictionary
empty_set = set()
