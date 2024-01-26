try:
    # with open opens the file without it needing to be closed
    with open('C:\\Users\\mathe\\Desktop\\py\\files\\test.txt') as file: # (path) if file is not in same directory
        print(file.read())

        #with open('test.txt','r'): if file is in same directory

    print(file.closed)  # displays true or false
except FileNotFoundError:
    print('file doesnt exist')

