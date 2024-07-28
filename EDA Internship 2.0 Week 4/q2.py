import pandas as pd

menu_df = pd.read_csv("menu.csv")
statistical_facts = menu_df.describe()
print(statistical_facts)
max_values = menu_df[['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber',
                      'Sugars', 'Protein', 'Vitamin A (% Daily Value)',
                      'Vitamin C (% Daily Value)', 'Calcium (% Daily Value)',
                      'Iron (% Daily Value)']].max()
print("\nMaximum values:")
print(max_values)