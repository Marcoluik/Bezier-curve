import numpy as np
import matplotlib.pyplot as plt


p0 = np.array([-1, 0])
p1 = np.array([2, 4])


t = np.linspace(0, 1, 100)


x = 3 * t - 1
y = 4 * t


plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$b(t) = (3t - 1, 4t)$')
plt.scatter(*p0, color='red', label='$p_0 = (-1, 0)$')
plt.scatter(*p1, color='blue', label='$p_1 = (2, 4)$')


plt.text(-1, 0, '  $p_0$', fontsize=12, verticalalignment='bottom')
plt.text(2, 4, '  $p_1$', fontsize=12, verticalalignment='bottom')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Linear Bézier Curve and Control Points')
plt.legend()
plt.grid(True)
plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.show()
