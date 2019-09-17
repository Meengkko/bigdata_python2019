import re

file_name_list = ["foo.bar", "autoexec.bat", "sendmail.cf"]


p = re.compile('.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$')
for file_name in file_name_list:
    print(p.search(file_name))
