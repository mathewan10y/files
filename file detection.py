import os

path='C:\\Users\\mathe\\Desktop\\py\\files\\test.txt'

if os.path.exists(path):
    print('that location exists')
    if os.path.isfile(path):
        print('that is a file')
    if os.path.isdir(path):
        print('that is a folder')
else:
    print('location doesnt exist')