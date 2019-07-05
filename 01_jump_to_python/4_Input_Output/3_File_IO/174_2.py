f = open("새파일.txt", 'r', encoding='UTF-8')
while True:
    line = f.readline()
    if not line: break
    print(line, end="") # 아스키 모드 파일을 print함수로 읽을 경우에는
                        # 줄바꿈의 왜곡이 일어날 수 있으므로 end=""를 반드시 사용한다.

f.close()