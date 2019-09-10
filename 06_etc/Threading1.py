import threading


def execute(number):  # 쓰레드로 실행할 함수 선언
    print(threading.currentThread().getName(), number)


if __name__ == '__main__':
    for i in range(1, 8):
        my_thread = threading.Thread(target=execute, args=(i,))  # 함수 할당
        my_thread.start()  # 메소드 호출
