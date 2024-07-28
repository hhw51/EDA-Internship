import pandas as pd

df = pd.read_excel('SampleWork.xlsx', sheet_name='Sheet1', header=None, skiprows=1, usecols=[0, -1])
df.columns = df.iloc[0]
df = df.drop(0)
df.to_excel('NewSheet.xlsx', index=False)
