# f = open('test.txt', 'r') # read a file (default)
# f = open('test.txt', 'w') # write to a file
# f = open('test.txt', 'a') # appending to a file
# f = open('test.txt', 'r+') # read and write to a file

f = open('test.txt')
print(f.name)
f.close()