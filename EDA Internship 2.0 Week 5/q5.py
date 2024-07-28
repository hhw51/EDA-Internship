import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Instagram data.csv", encoding='latin1')
plt.plot(df.index, df['Impressions'])
plt.xlabel('Index')
plt.ylabel('Impressions')
plt.title('Impressions Over Time')
plt.show()
