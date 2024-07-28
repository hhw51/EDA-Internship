import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Instagram data.csv", encoding='latin1')
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Likes'], color='blue', label='Likes', marker='o')
plt.plot(df.index, df['Saves'], color='red', label='Saves', marker='o')
plt.plot(df.index, df['Follows'], color='green', label='Follows', marker='o')
plt.xlabel('Post')
plt.ylabel('Count')
plt.title('Metrics for Each Post')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
