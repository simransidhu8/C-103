import plotly.express as px
import pandas as pd

df = pd.read_csv("data.csv")
fig = px.bar(df, x = "Country", y="InternetUsers", color="Country", title= "Internet Users in Countries")
fig.show()