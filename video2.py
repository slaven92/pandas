import pandas as pd
import matplotlib as plt
# %%
df = pd.read_csv(
    "Y:/Slaven/pythonStuff/projects/pandas/avocado-prices/avocado.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.copy()[df["type"] == "organic"]
# %%
albany_df = df.copy()[df['region'] == "Albany"]
albany_df.set_index("Date", inplace=True)
# %%
albany_df.sort_index(inplace=True)
albany_df["AveragePrice"].rolling(25).mean().plot()

albany_df['price25ma'] = albany_df["AveragePrice"].rolling(25).mean()
albany_df.tail()

# %%

df["region"].unique()
graph_df = pd.DataFrame()

for region in df["region"].unique():
    print(region)
    region_df = df.copy()[df["region"] == region]
    region_df.set_index("Date", inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f'{region}_price25ma'] = region_df["AveragePrice"].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f'{region}_price25ma']]
    else:
        graph_df = graph_df.join(region_df[f'{region}_price25ma'])

# %%
graph_df.dropna().plot(figsize=(10,10),legend=False)
