import matplotlib.pyplot as plt
import pandas as pd

data = {
    'a': [4, 2, 4, 2, 2],
    'b': [8, 3, 7, 6, 4],
    'c': [5, 4, 4, 4, 3],
    'd': [7, 2, 7, 8, 3],
    'e': [6, 6, 8, 6, 2]
}

df = pd.DataFrame(data, index=[2, 4, 6, 8, 10])

fig, ax = plt.subplots()
colors = ['blue', 'darkgreen', 'red', 'lightblue', 'purple']

df.plot(kind='bar', ax=ax, color=colors)

ax.set_xticks(range(len(df.index)))
ax.set_xticklabels(df.index, rotation=0)

plt.show()