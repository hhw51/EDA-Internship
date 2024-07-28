import pandas as pd

df = pd.read_csv("instagram data.csv", encoding='latin1')
print("Column Names and Info:")
print(df.info())
