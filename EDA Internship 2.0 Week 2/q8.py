import pandas as pd

data = {
    'Name': ['Sonia', 'Bilal', 'Hifza', 'Kabir', 'Jazim'],
    'Age': [27, 24, 22, 32, 23],
    'Address': ['Lahore', 'Karachi', 'Sialkot', 'Peshawar', 'Lhr'],
    'Qualification': ['Msc', 'MA', 'MCA', 'Phd', 'bsc']
}
AICP_DF = pd.DataFrame(data)
df1 = AICP_DF[['Name', 'Qualification']]
AICP_DF['Height'] = [5.1, 6.2, 5.1, 5.2, 5.1]
AICP_DF.set_index('Name', inplace=True)
row_hifza = AICP_DF.loc['Hifza']
row_index_3 = AICP_DF.iloc[2]
AICP_DF.drop(index='Bilal', inplace=True)

print("AICP_DF:")
print(AICP_DF)
print("\nDataFrame df1:")
print(df1)
print("\nRow with index 'Hifza':")
print(row_hifza)
print("\nRow with index 3:")
print(row_index_3)
