import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

menu_df = pd.read_csv("menu.csv")
numeric_columns = menu_df.select_dtypes(include=['number'])
correlation_matrix = numeric_columns.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()
