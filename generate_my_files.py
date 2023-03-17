import os
count = 0 
#where are we going to write  the file and 'my_files' will be the name
with open('C:/Users/nerina/Documents/GitHub/filesizes/my_files.py', 'w', encoding='utf-8', errors='ignore') as _files:#w means write
    _files.write('files = [\n')

with open('C:/Users/nerina/Documents/GitHub/filesizes/my_files.py', 'a', encoding='utf-8', errors='ignore') as _files:#a means append
    
    for root, directories, files in os.walk('/Users/nerina/Documents'):# where we are going to search
        for _file in files:
            if count > 20:
                break
            try:
                full_path = os.path.join(root, _file)
                size = os.path.getsize(full_path)
            except (FileNotFoundError,PermissionError):
                continue
            _files.write(f"('{full_path}', {size}),\n")
            
            count += 1
    _files.write(']')
