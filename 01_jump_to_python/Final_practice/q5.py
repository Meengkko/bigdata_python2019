def fibonacci(max):
    fib_one = 0
    fib_two = 1
    while fib_one <= max:
        print(f"{fib_one}", end=' ')
        fib_one, fib_two = fib_two, fib_one + fib_two


max_pivot = int(input("피보나치 수열을 출력할 상한을 입력해 주십시오. : "))
fibonacci(max_pivot)
