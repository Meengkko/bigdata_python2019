import matplotlib.pyplot as plt

plt.figure()

plt.subplot(1, 2, 1)
plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'r-')
plt.subplot(1, 2, 2)
plt.plot([1, 2, 3, 4], [4, 3, 2, 1], 'b-')
plt.show()