#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

N = 500
normal = np.random.normal(loc=0.0, scale=1.0, size=N)
lognormal = np.random.lognormal(mean=0.0, sigma=1.0, size=N)
box_plot_data = [normal, lognormal]

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

box_labels = ['normal', 'lognormal']
# notch: False => 상자 중간의 홈(notch)이 파이지 않도록 한다.
# sym: '.' 특이사항을 '.'dmfh vytl
# vert: 세로(vertical)로 표기
# wixh: 제 1사분위수 및 제 3사분위수를 연장한 수염의 길이 지정(1.5를 사용할 것)
ax1.boxplot(box_plot_data, notch=False, sym='.', vert=True, whis=1.5, showmeans=True, labels=box_labels)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Box Plots: Resampling of Two Distributions')
ax1.set_xlabel('Distribution')
ax1.set_ylabel('Value')

plt.savefig('box_plot.png', dpi=400, bbox_inches='tight')
plt.show()
