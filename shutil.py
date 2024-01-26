'''copyfile - copies contents of a file
   copy()  - copyfile() + permission mode + destination can be a directory
   copy2() - copy() + metadata ( file's creation and modification times)'''

import shutil
shutil.copy('text.txt','copy.txt') # (source,destination)