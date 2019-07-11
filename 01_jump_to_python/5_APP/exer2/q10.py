import os
import time

os.chdir("C:/Python_Workspace/01_jump_to_python")

f = os.popen('dir')
print(f.read())

time.sleep(2)
os.system('cls')
