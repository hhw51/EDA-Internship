import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Instagram data.csv", encoding='latin1')
numeric_df = df.select_dtypes(include=['number'])
correlation_matrix = numeric_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Between Numeric Features')
plt.show()
