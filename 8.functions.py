# def hello_func():
#     pass 

# hello_func()
# print(hello_func())

# def hello_func():
#     # print('Hello function!') 
#     return 'Hello function!'

# hello_func()
# print(hello_func())
# print(hello_func().upper())

# def hello_func(greeting):
#     return '{} Function.'.format(greeting)

# print(hello_func('Hi'))

# def hello_func(greeting, name='You'):
#     return '{}, {}'.format(greeting, name)

# print(hello_func('Hi', name='Ukeme')) # args before kwargs

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# student_info('Math', 'Art', name='John', age=22)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name':'John', 'age':22}

student_info(*courses, **info)