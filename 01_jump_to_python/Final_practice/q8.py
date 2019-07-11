with open("ABC.txt", 'r') as abc_file:
    abc_lines = abc_file.readlines()

with open("ABC.txt", 'w') as reverse_abc:
    for i in range(1, len(abc_lines)+1):
        reverse_abc.write(abc_lines[len(abc_lines)-i])
