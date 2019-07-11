def my_add(a, b):
    return a + b


def my_sub(a, b):
    return a - b

# 아래와 같이 테스트 코드로서 동작하기 위한 용도로
# 조건을 체크하는 코드를 'Boilerplate Code'라고 한다.
if __name__ == "__main__":
    print(my_add(3, 4))
    print(my_sub(3, 4))
