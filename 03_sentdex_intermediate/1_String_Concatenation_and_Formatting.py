names = ['Jeff', 'Gary', 'Jill', 'Samantha']

# for name in names:
    # print("Hello there, " + name)
    # print(' '.join(['Hello there,', name]))

# print(', '.join(names))

import os

location_of_file = 'C:/Python_Workspace/03_sentdex_intermediate'
file_name = 'example.txt'

print(location_of_file + '/' + file_name)

with open(os.path.join(location_of_file, file_name)) as f:
    print(f.read())
