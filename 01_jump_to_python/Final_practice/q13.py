def is_duplicated_even_odd(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return 1
    elif num1 % 2 == 1 and num2 % 2 == 1:
        return -1
    return 0


result = input("숫자 입력")
i = 0
while i < len(result) - 1:
    try:
        if is_duplicated_even_odd(int(result[i]), int(result[i+1])) == 1:
            result = result[:i + 1] + "*" + result[i + 1:]
        elif is_duplicated_even_odd(int(result[i]), int(result[i+1])) == -1:
            result = result[:i + 1] + "-" + result[i + 1:]
    except ValueError:
        pass
    i += 1

print(result)
