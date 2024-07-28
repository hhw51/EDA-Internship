import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.barh(languages, popularity, color='green', height=0.3)
plt.tick_params(axis='y', which='major', labelsize=8)
plt.xlabel('Popularity')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages \n WorldWide, Oct 2017 compared to a year ago')
plt.grid(True)
plt.show()
