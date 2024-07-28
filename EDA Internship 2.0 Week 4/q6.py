import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

menu_df = pd.read_csv("menu.csv")
attributes = ['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars', 'Protein',
              'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)', 'Calcium (% Daily Value)',
              'Iron (% Daily Value)']
for attribute in attributes:
    plt.figure(figsize=(12, 6))
    sns.stripplot(x='Category', y=attribute, data=menu_df, jitter=True)
    plt.title(f'Stripplot of {attribute} Across Categories')
    plt.xlabel('Category')
    plt.ylabel(attribute)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(f'stripplot_{attribute}.png')
    plt.close()
