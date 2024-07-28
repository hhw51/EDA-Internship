import matplotlib.pyplot as plt

x_red = [10, 15, 20, 25, 30]
y_red = [40, 25, 10, 20, 30]

x_blue = [10, 15, 20, 25, 30]
y_blue = [20, 25, 40, 25, 10]

plt.plot(x_red, y_red, color='red', linewidth=5, label='Red Line')
plt.plot(x_blue, y_blue, color='blue', linewidth=3, label='Blue Line')
plt.legend()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Lines Plot')
plt.grid(True)
plt.show()
