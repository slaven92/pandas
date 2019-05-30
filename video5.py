import pandas as pd
import numpy as np

unemp_country = pd.read_csv("Y:/Slaven/pythonStuff/projects/pandas/unemployment-by-county-us/output.csv")

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
act_min_wage = act_min_wage.replace(0, np.NaN).dropna(axis=1)
act_min_wage.head()

# %%
def get_min_wage(year, state):
    try:
        return act_min_wage.loc[year][state]
    except:
        return np.NaN
get_min_wage(1968, "Alaska")

# %%
unemp_country['min_wage'] = list(map(get_min_wage,unemp_country["Year"], unemp_country['State']))
unemp_country.head()

unemp_country[["Rate", "min_wage"]].corr()
unemp_country[["Rate", "min_wage"]].cov()

# %%
pres16 = pd.read_csv("Y:/Slaven/pythonStuff/projects/pandas/2016uspresidentialvotebycounty/pres16results.csv")

county_2015 = unemp_country[(unemp_country['Year']==2015) & (unemp_country['Month'] == "February")]
county_2015.head()

# %%
import requests
web = requests.get("https://www.infoplease.com/us/postal-information/state-abbreviations-and-state-postal-codes", params=None)
dfs = pd.read_html(web.text)
state_abbv = dfs[0]
state_abbv.set_index("State/District", drop=True, append=False, inplace=True, verify_integrity=False)
abbv_dict = state_abbv[["Postal Code"]].to_dict()
abbv_dict = abbv_dict["Postal Code"]
abbv_dict['Federal (FLSA)'] = "FL"
abbv_dict['Guam'] = "GU"
abbv_dict['Puerto Rico'] = "PR"

county_2015['State'] = county_2015["State"].map(abbv_dict)

county_2015.tail()

# %%
pres16.rename(columns = {"county":"County", "st":"State"}, inplace = True)
pres16.head(n=5)

for df in [county_2015, pres16]:
    df.set_index(["County", "State"], inplace=True)
pres16 = pres16[pres16["cand"] == "Donald Trump"]
pres16 = pres16[["pct"]]
pres16.dropna(inplace = True)
pres16.head()

all_together = county_2015.merge(pres16, on = ["County", "State"])
all_together.dropna(inplace = True)
all_together.drop("Year", axis=1, inplace = True)
all_together.head()

# %%
all_together.corr()
all_together.cov()
