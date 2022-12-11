"""
LEGB
Local Enclosing Global Built-in

Local -> Variables within a function
Enclosing -> Variables in local scope of an enclosing function
Global -> Variables declared at the top level of a module of explicitly declared with a global keyword
Built-in -> Names that are pre-assigned in python
"""

# x = 'global x'

# def test():
#     # global x
#     y = 'local y'
#     # print(y)
#     # print(x)
#     x = 'local x'
#     print(x)

# test()
# print(y)
# print(x)

# def test(z):
#     print(z)

# test('local z')

#Built-in

m = min([5, 1, 4, 2, 3])
print(m)

#Enclosing

def outer():
    x = 'outer x'
    
    def inner():
        nonlocal x
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()

