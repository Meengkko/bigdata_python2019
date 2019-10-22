# 목적: 기본 그래프 그리기

import matplotlib.pyplot as plt

# plt.plot([2, 1, 4, 3], [1, 3, 2, 5])
# plt.plot([2, 1, 4, 3], [1, 3, 2, 5], 'ro')
plt.plot([2, 1, 4, 3], [1, 3, 2, 5], 'bo')
# plt.plot([2, 1, 4, 3], [1, 3, 2, 5], 'bx')
# plt.plot([2, 1, 4, 3], [1, 3, 2, 5], 'bv')
plt.xlabel('x_axis_label')
plt.ylabel('y_axis_label')
plt.show()
