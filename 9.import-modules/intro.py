# import my_module
# import my_module as m
# from my_module import find_index, test
# from my_module import find_index as fi, test
# from my_module import * # import everything
import sys
sys.path.append('/Users/Bassey Ukeme/Desktop')
from py_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
# print(index)
# print(test)
print(sys.path)
