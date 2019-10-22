# 목적: 하나의 차트에 다수의 그래프 그리기, 한글 처리
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

font_location = 'C:\Windows\Fonts\malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)

plt.plot([1, 2, 3, 4, 8], [1, 2, 3, 8, 16], 'v-', [1, 6, 7, 8], [5, 6, 7, 15], 'v-')
plt.xlabel('x축 라벨')
plt.ylabel('y축 라벨')
plt.show()
