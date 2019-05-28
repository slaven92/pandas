import pandas as pd

df = pd.read_csv("/home/slaven92/Downloads/avocado.csv")

df["AveragePrice"].head(5)

albany_df = df[df["region"] == "Albany"]

albany_df.tail()
