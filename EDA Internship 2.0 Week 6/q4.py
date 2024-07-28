import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("births.csv")
df['Decade'] = (df['year'] // 10) * 10
trend = df.groupby(['Decade', 'gender'])['births'].sum().unstack()
trend.plot(kind='line', marker='o')
plt.title('Trend of Male & Female Births Every Decade')
plt.xlabel('Decade')
plt.ylabel('Number of Births')
plt.xticks(ticks=trend.index, labels=trend.index)
plt.grid(True)
plt.legend(title='Gender')
plt.show()
