import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

df = pd.read_csv("Instagram data.csv", encoding='latin1')
all_hashtags = df['Hashtags'].str.split()
all_hashtags_flat = [tag for sublist in all_hashtags for tag in sublist]
hashtag_counts = Counter(all_hashtags_flat)
most_common_hashtag, most_common_count = hashtag_counts.most_common(1)[0]
plt.figure(figsize=(10, 6))
hashtag_counts_df = pd.DataFrame(hashtag_counts.most_common(10), columns=['Hashtag', 'Count'])
plt.bar(hashtag_counts_df['Hashtag'], hashtag_counts_df['Count'], color='skyblue')
plt.title('Top 10 Most Used Hashtags')
plt.xlabel('Hashtag')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
print(f"The most commonly used hashtag is '{most_common_hashtag}' with a count of {most_common_count}.")