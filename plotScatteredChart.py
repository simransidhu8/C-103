import plotly.express as px
import pandas as pd

df = pd.read_csv("data.csv")
fig = px.scatter(df, x="Population", y="Per capita", color = "Country", title="Internet Users", size="Percentage", size_max=60)
fig.show()