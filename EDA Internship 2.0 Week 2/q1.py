import pandas as pd

ind = ['a', 'x', 'c', '2', 'e']
arr = [1, 4, 9, 6, 7]

ser = pd.Series(arr,ind)
print(ser)