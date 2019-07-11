import os

print(os.getcwd())
# os.system('dir')
# os.system("notepad my_info.txt")
# os.system("\"C:\Program Files (x86)\Microsoft Office\Office14\POWERPNT\"")
# os.system("\"C:\Program Files\Internet Explorer\iexplore\"")

# 아래 위로 프로그램이 순차적으로 실행된다. 동시에 실행시키려면 스레드를 활용해야 한다.

# 경로변경 후
# os.system("notepad .\my_info\my_info.txt")
# os.chdir('./my_info')
# os.system('my_info.txt')

f = os.popen('dir')
print(f.read())
