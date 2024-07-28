import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

menu_df = pd.read_csv("menu.csv")

menu_df = menu_df[['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber',
                   'Sugars', 'Protein', 'Vitamin A (% Daily Value)',
                   'Vitamin C (% Daily Value)', 'Calcium (% Daily Value)',
                   'Iron (% Daily Value)']]
print(menu_df)