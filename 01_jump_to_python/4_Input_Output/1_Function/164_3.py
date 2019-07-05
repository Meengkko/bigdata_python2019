a = 10


def vartest():
    print(a) # 전역 변수를 단순히 조회하는 것은 문제가 없다.


# def vartest2():
#     print(a)
#     a=a+1 # 지금과 같은 방식으로 전역변수의 값을 수정할 수 없다.
#     print(a)


def vartest3():
    global a
    print(a)
    a=a+1 # 지금과 같은 방식으로 전역변수의 값을 수정할 수 없다.
    print(a)


vartest()
# vartest2()
vartest3()

print(a)