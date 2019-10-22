# 히스토그램
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

mu1, mu2, sigma1, sigma2 = 100, 200, 50, 300

x1 = mu1 + sigma1 * np.random.randn(15000)
x2 = mu2 + sigma2 * np.random.randn(10000)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# bins: 수치가 클수록 세로축이 정교해짐
# normed: False일 경우 확률이 아니라 빈도로 표시
# alpha: 투명도
n, bins, patched = ax1.hist(x1, bins=50, normed=False, color='darkgreen', alpha=0.7)
n, bins, patched = ax1.hist(x2, bins=50, normed=False, color='darkred', alpha=0.5)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
fig.suptitle('Histogram', fontsize=14, fontweight='bold')
ax1.set_title('Two Frequency Distributions')

plt.savefig('histogram.png', dpi=400, bbox_inches='tight')
plt.show()
