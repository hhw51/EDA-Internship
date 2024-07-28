import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Instagram data.csv", encoding='ISO-8859-1')
reach_from_home = df['From Home'].sum()
reach_from_hashtags = df['From Hashtags'].sum()
reach_from_explore = df['From Explore'].sum()
reach_from_other = df['From Other'].sum()

plt.figure(figsize=(8, 8))

colors = ['pink', 'blue', 'green', 'orange']

plt.pie([reach_from_home, reach_from_hashtags, reach_from_explore, reach_from_other],
        labels=['From Home', 'From Hashtags', 'From Explore', 'From Other'],
        colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Reach from Different Sources')
plt.axis('equal')
plt.show()

