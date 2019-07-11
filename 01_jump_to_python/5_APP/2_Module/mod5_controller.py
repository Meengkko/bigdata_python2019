# from ./my_mod/mod5 import * # 모듈은 왼쪽 코드와 같이 상대경로가 불가능하다.
import sys
# 개발 중에는 모듈 경로를 파이참에 추가하고
# 배포시에는 경로를 코드상에 추가한다.
# sys.path.append('C:/Python_Workspace/01_jump_to_python/5_APP/2_Module/my_mod')
# sys.path.append('./my_mod')
# 파이썬 코드를 기준으로한 상대경로 추가가능
sys.path.append('my_mod2')

from mod6 import *

print("mod5 controller ver1 initializing...")
input("초기화가 완료되었습니다. 구동하시겠습니까?")

num1 = int(input("첫번째 수를 입력하세요: "))
num2 = int(input("두번째 수를 입력하세요: "))


print('자! 그럼 입력받은 두 수에 대한 덧셈과 뺄셈 결과를 출력합니다.')
print(my_add(num1, num2))
print(my_sub(num1, num2))
