
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
menu_df = pd.read_csv("menu.csv")

# Draw boxplot for Calories vs Category
plt.figure(figsize=(12, 8))
sns.boxplot(x='Category', y='Calories', data=menu_df)
plt.title('Calories Distribution Across Categories')
plt.xticks(rotation=90)
plt.xlabel('Category')
plt.ylabel('Calories')
plt.show()
