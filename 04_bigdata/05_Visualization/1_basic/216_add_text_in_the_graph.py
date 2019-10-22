# 목적: 그래프 문자입력하기
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

font_location = "C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)

plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'y')
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('matplotlib 활용')
plt.text(3.5, 3.0, '평균: 2.5')
plt.grid(True)

plt.show()
