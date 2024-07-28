import pandas as pd

df = pd.read_csv("births.csv")
mean = df['births'].mean()
std_dev = df['births'].std()
lower_bound = mean - 5 * std_dev
upper_bound = mean + 5 * std_dev
df_filtered = df[(df['births'] >= lower_bound) & (df['births'] <= upper_bound)]
print(df_filtered)