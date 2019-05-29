import pandas as pd
import matplotlib as plt
# %%
df = pd.read_csv(
    "Y:/Slaven/pythonStuff/projects/pandas/us-minimum-wage-by-state-from-1968-to-2017/Minimum Wage Data.csv", encoding='latin')

gb = df.groupby('State')
gb.get_group('Alabama').set_index('Year').head()

# %%
act_min_wage = pd.DataFrame()

for name, group in df.groupby('State'):
    if act_min_wage.empty:
        act_min_wage = group.set_index('Year')[['Low.2018']].rename(columns={'Low.2018':name})
    else:
        act_min_wage = act_min_wage.join(group.set_index('Year')[['Low.2018']].rename(columns={'Low.2018':name}))
