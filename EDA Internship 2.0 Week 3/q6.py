import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
print(df.columns)
df = df.sort_values(by='gold_medal', ascending=False)
top_countries = df.head(5)
plt.figure(figsize=(8, 8))
plt.pie(top_countries['gold_medal'], labels=top_countries['country'], autopct='%1.1f%%', startangle=140)
plt.title('Gold Medal Achievements of Top 5 Countries in 2016 Summer Olympics')
plt.axis('equal')
plt.show()

