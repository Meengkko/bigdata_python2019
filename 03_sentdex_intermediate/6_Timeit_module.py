import timeit
# print(timeit.timeit('1+3', number=500000000))


input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in input_list if div_by_five(i))

for i in xyz:
    print(i)
# print([i for i in xyz])
#
# xyz = [i for i in input_list if div_by_five(i)]
#
# print(xyz)


# print(timeit.timeit("""input_list = range(100)
#
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
#
# xyz = list((i for i in input_list if div_by_five(i)))
# """, number=5000))
# 다써줘야한다

print(timeit.timeit('''input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in input_list if div_by_five(i))

for i in xyz:
    x = i
''', number=5000))