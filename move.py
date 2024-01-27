
# we can move a file using os.replace(source,destination)


import os
source='move.txt'
destination='C:\\Users\\mathe\\Desktop\\py\\dictionary\\move.txt'

try:
    if os.path.exists(destination):
        print('there is already a destination')
    else:
        os.replace(source,destination)
        print(source,'was moved')



except FileNotFoundError:
    print('file was not found')

