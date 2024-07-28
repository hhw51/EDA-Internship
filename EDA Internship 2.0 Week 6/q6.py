import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("births.csv")
df['year'] = df['year'].astype(str)
df['month'] = df['month'].astype(str).str.zfill(2)  # Zero-padding for months < 10
df['day'] = df['day'].astype(str).str.zfill(2)      # Zero-padding for days < 10
df['date'] = df['year'] + '-' + df['month'] + '-' + df['day']
df['date'] = pd.to_datetime(df['date'])
df['weekday'] = df['date'].dt.day_name()

def get_decade(year):
    return str(year // 10 * 10) + 's'

df['decade'] = df['year'].apply(get_decade)
grouped = df.groupby(['decade', 'weekday'])['births'].sum().unstack()
grouped.plot(kind='bar', figsize=(10, 6))
plt.title('Births by Weekday for Several Decades')
plt.xlabel('Decade')
plt.ylabel('Number of Births')
plt.xticks(rotation=45)
plt.legend(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.show()
