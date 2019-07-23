# import math
#
# def solution(progresses, speeds):
#     remain = list(map(lambda x, y: math.ceil((100 - x)/y), progresses, speeds))
#     answer = []
#     count = 1
#     remain.append(9999)
#     for i in range(len(remain)-1):
#         if remain[i] >= remain[i+1]:
#             count += 1
#         else:
#             answer.append(count)
#             count = 1
#     return answer
#
#
# print(solution([97, 30, 55], [1, 30, 5]))

import time

input("A")
time.sleep(1)
input("B")
time.sleep(2)