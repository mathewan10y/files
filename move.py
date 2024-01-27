
# we can move a file using os.replace(source,destination)


import os
source='C:\\Users\\mathe\\Desktop\\py\\files\\move.txt'
destination='C:\\Users\\mathe\\Desktop\\move.txt'

try:
    if os.path.exists(destination):
        print('there is already a destination')
    else:
        os.replace(source,destination)
        print(source,'was moved')



except FileNotFoundError:
    print('file was not found')

# move.txt file was moved from files to the desktop