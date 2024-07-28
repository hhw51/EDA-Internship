import pandas as pd

data = pd.read_csv('people.csv', skiprows=[1, 5])
col = ["Sex", "Job Title", "First Name", "Email", "Phone"]
data = data[col]
data.set_index(["Sex", "Job Title"], inplace=True)
data.to_csv('NewPeople.csv')