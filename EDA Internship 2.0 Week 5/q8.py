import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Instagram data.csv", encoding='latin1')
engagement_df = df[['Likes', 'Saves', 'Shares', 'Comments']]
engagement_totals = engagement_df.sum()
plt.figure(figsize=(8, 6))
colors = ['pink', 'blue', 'green', 'orange']
sources = ['Likes', 'Saves', 'Shares', 'Comments']

plt.pie(engagement_totals,
        labels=sources,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors)

plt.title('Distribution of Engagement Sources')
plt.axis('equal')
plt.show()
