# f = open('test.txt', 'r') # read a file (default)
# f = open('test.txt', 'w') # write to a file
# f = open('test.txt', 'a') # appending to a file
# f = open('test.txt', 'r+') # read and write to a file

# f = open('test.txt', 'r')
# # print(f.name)
# print(f.mode)
# f.close()

with open('test.txt', 'r') as f:
    # f_contents = f.read()
    # f_contents = f.readlines()
    # f_contents = f.readline()
    # print(f_contents)

    # f_contents = f.readline()
    # print(f_contents)

    # f_contents = f.readline()
    # print(f_contents)

    # f_contents = f.readline()
    # print(f_contents)
    # for line in f:
    #     print(line, end='')

    # f_contents = f.read(30)
    # print(f_contents, end='')

    # f_contents = f.read(30)
    # print(f_contents, end='')


    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)

# print(f.closed)