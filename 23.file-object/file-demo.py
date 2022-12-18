# f = open('test.txt', 'r') # read a file (default)
# f = open('test.txt', 'w') # write to a file
# f = open('test.txt', 'a') # appending to a file
# f = open('test.txt', 'r+') # read and write to a file

# f = open('test.txt', 'r')
# # print(f.name)
# print(f.mode)
# f.close()

# with open('test.txt', 'r') as f:
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


    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # while len(f_contents) > 0:
    #     print(f_contents, end='')
    #     f_contents = f.read(size_to_read)

    # print(f.tell())

    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')

    # f.seek(4) # set the position back to the beginning of the file

    # f_contents = f.read(size_to_read)
    # print(f_contents)
    

# print(f.closed)


# with open('test2.txt', 'w') as f:
#     f.write('Test')

# with open('test.txt' , 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# with open('ukeme.jpg' , 'rb') as rf:
#     with open('ukeme_copy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

with open('ukeme.jpg' , 'rb') as rf:
    with open('ukeme_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
            