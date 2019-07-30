## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
print(avengers.head(5))

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = avengers[avengers['Year'] > 1960]

avengers['Year'].hist()

## 5. Consolidating Deaths ##

def count_death(row):
    count = 0
    cols = ['Death1','Death2','Death3','Death4','Death5']
    for each in cols:
        if pd.isnull(row[each]) or row[each] == 'NO':
            continue
        elif row[each] == 'YES':
            count += 1
    return count

true_avengers['Deaths'] = true_avengers.apply(count_death,axis=1)

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()
count = 0
accurate = true_avengers['Year'] == (2015 - true_avengers['Years since joining'])
joined_accuracy_count = len(accurate)