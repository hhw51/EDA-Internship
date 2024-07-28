import matplotlib.pyplot as plt

x_red = [1, 4, 5, 6, 7]
y_red = [2, 6, 3, 6, 3]
plt.plot(x_red, y_red, color='red', linestyle='dotted', marker='o', markersize=10, markerfacecolor='blue', label='Red Line')
plt.legend()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line Plot with Markers')
plt.grid(True)
plt.show()
