import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Instagram data.csv", encoding='latin1')

profile_visits = df['Profile Visits']
follows = df['Follows']
plt.figure(figsize=(8, 6))
plt.scatter(profile_visits, follows, color='blue', alpha=0.5)
plt.title('Relationship between Profile Visits and Follows')
plt.xlabel('Profile Visits')
plt.ylabel('Follows')
plt.grid(True)
plt.show()
