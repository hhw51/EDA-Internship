import pandas as pd
import plotly.express as px

df = pd.read_csv("Instagram data.csv", encoding='latin1')

fig = px.histogram(df, x="Impressions", title="Distribution of Impressions")

fig.write_image("impressions_distribution.png")