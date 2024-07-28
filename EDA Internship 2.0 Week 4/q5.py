import pandas as pd

menu_df = pd.read_csv("menu.csv")
max_values = menu_df[['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars',
                      'Protein', 'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)',
                      'Calcium (% Daily Value)', 'Iron (% Daily Value)']].idxmax()
max_items = menu_df.loc[max_values]
max_items.to_csv('max_values_summary.csv', index=False)
