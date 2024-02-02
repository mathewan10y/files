import os 

path='C:\\Users\\mathe\\Desktop\\move.txt'
try:
    os.rmdir(path) # to delete empty files

 #   os.remove(path) to delete non-empty files
except FileNotFoundError:
    print('file doesnt exist')
except PermissionError:
    print('you dont have permission to delete this file')
except