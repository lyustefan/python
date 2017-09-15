## 2. Introduction to the Data ##

import pandas as pd
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
all_ages[:5]
recent_grads[:5]

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()


def count(df):
    counts = dict()
    df_unique = df["Major_category"].unique()
    for a in df_unique:
        major_row = df[df["Major_category"] == a]
        major_sum = major_row["Total"].sum()
        counts[a] = major_sum    
    return counts

aa_cat_counts = count(all_ages)
rg_cat_counts = count(recent_grads)

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0
low_wage_percent = recent_grads["Low_wage_jobs"].sum() / recent_grads["Total"].sum()

print(low_wage_percent)


## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for major in majors:
    age_row = all_ages[all_ages["Major"]== major]
    grad_row = recent_grads[recent_grads["Major"] == major]
    age_um = age_row.iloc[0]["Unemployment_rate"]
    grad_um = grad_row.iloc[0]["Unemployment_rate"]
    
    if age_um > grad_um:
        rg_lower_count += 1
print(age_row)
print(rg_lower_count)
    