import pandas as pd
import matplotlib as plt

# df = pd.read_csv("/home/slaven92/Downloads/avocado.csv")
df = pd.read_csv("Y:/Slaven/pythonStuff/projects/pandas/avocado-prices/avocado.csv")

df["AveragePrice"].head(5)

albany_df = df[df["region"] == "Albany"]

albany_df.tail()

albany_df.index

albany_df.set_index("Date", inplace=True)

albany_df.head()
albany_df_organic = albany_df[albany_df["type"] == "organic"]
albany_df_conventional = albany_df[albany_df["type"] == "conventional"]

albany_df_organic['AveragePrice'].plot()
albany_df_conventional['AveragePrice'].plot()
