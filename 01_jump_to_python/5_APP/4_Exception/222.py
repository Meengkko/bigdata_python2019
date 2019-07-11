print('작업1')
f = open("나없는파일", 'r')
# 파일이 없는 경우 아래와 같은 메세지를 발생하고 런타임 에러를 발생한다.
# FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'
# 이 때 프로그램은 강제종료된다.
print('작업2')
print('프로그램 정상종료')