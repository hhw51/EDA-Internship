import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv("Instagram data.csv", encoding='latin1')

hashtags_text = ' '.join(df['Hashtags'])

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(hashtags_text)

plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Word Cloud of Hashtags')
plt.axis('off')  # Hide the axes
plt.show()