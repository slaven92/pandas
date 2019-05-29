import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
    "Y:/Slaven/pythonStuff/projects/pandas/us-minimum-wage-by-state-from-1968-to-2017/Minimum Wage Data.csv", encoding='latin')
act_min_wage = pd.DataFrame()

for name, group in df.groupby('State'):
    if act_min_wage.empty:
        act_min_wage = group.set_index(
            'Year')[['Low.2018']].rename(columns={'Low.2018': name})
    else:
        act_min_wage = act_min_wage.join(group.set_index(
            'Year')[['Low.2018']].rename(columns={'Low.2018': name}))
# act_min_wage.replace(0, np.NaN).dropna(axis=1).corr().head()
min_wage_corr = act_min_wage.replace(0,np.NaN).dropna(axis=1).corr()

min_wage_corr.head()
# %%

labels = [c[:2] for c in min_wage_corr.columns]
fig = plt.figure(figsize=(11,11))
ax = fig.add_subplot(111)
ax.set_yticklabels(labels)
ax.set_xticklabels(labels)
ax.matshow(min_wage_corr, cmap = plt.cm.RdYlGn)
ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(labels)))
plt.show()

# %%
import requests
web = requests.get("https://www.infoplease.com/us/postal-information/state-abbreviations-and-state-postal-codes", params=None)
dfs = pd.read_html(web.text)
state_abbv = dfs[0]
state_abbv.set_index("State/District", drop=True, append=False, inplace=True, verify_integrity=False)
abbv_dict = state_abbv[["Postal Code"]].to_dict()
abbv_dict = abbv_dict["Postal Code"]
abbv_dict
# %%
abbv_dict['Federal (FLSA)'] = "FL"
abbv_dict['Guam'] = "GU"
abbv_dict['Puerto Rico'] = "PR"
labels = [abbv_dict[c] for c in min_wage_corr.columns]
fig = plt.figure(figsize=(13,13))
ax = fig.add_subplot(111)
ax.set_yticklabels(labels)
ax.set_xticklabels(labels)
ax.matshow(min_wage_corr, cmap = plt.cm.RdYlGn)
ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(labels)))
plt.show()
