## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for each in data_files:
    a = pd.read_csv("schools/{0}".format(each))
    key_name = each.replace(".csv","")
    data[key_name] = a
    
    

## 5. Exploring the SAT Data ##

print(data["sat_results"].head(5))


## 6. Exploring the Remaining Data ##

for k,v in data.items():
    print(v.head(5))

## 8. Reading in the Survey Data ##

#Read in the all_survey datasets
all_survey = pd.read_csv("schools/survey_all.txt",delimiter="\t",encoding="windows-1252")
#Read in the d75_survey datasets
d75_survey = pd.read_csv("schools/survey_d75.txt",delimiter="\t",encoding="windows-1252")
# Use rowbinding to combine two datasets
survey = pd.concat([all_survey,d75_survey],axis=0)
print(survey.head())

## 9. Cleaning Up the Surveys ##

#Copy the original column named dbn to a new colum named DBN
survey["DBN"] = survey["dbn"]
cols = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
survey = survey.loc[:,cols]
data["survey"] = survey
data["survey"].info()


## 11. Inserting DBN Fields ##

data['hs_directory']["DBN"] = data['hs_directory']["dbn"]

def add_zero(number):
    str_n = str(number)
    if len(str_n) == 2:
        return str_n
    elif len(str_n) == 1:
        return str_n.zfill(2)

data["class_size"]['padded_csd'] = data["class_size"]["CSD"].apply(add_zero)

data["class_size"]['DBN'] = data["class_size"]['padded_csd'] + data["class_size"]['SCHOOL CODE']

    

## 12. Combining the SAT Scores ##

cols = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score','SAT Writing Avg. Score']
sat = data["sat_results"]
for each in cols:
    sat[each] = pd.to_numeric(sat[each],errors='coerce')

sat['sat_score'] = 0
for each in cols:
    sat['sat_score'] = sat['sat_score'] + sat[each]

print(sat['sat_score'])

## 13. Parsing Geographic Coordinates for Schools ##

import re
def lat(row):
    curr = re.findall("\(.+\)", row)
    lat = curr[0].split(",")[0].replace('(','')
    return lat

data['hs_directory']['lat'] = data["hs_directory"]['Location 1'].apply(lat)
data['hs_directory'].head()


        

## 14. Extracting the Longitude ##

import re
def lon(row):
    curr = re.findall("\(.+\)", row)
    lon = curr[0].split(",")[1].replace(')','').strip()
    return lon

data['hs_directory']['lon'] = data["hs_directory"]['Location 1'].apply(lon)

data['hs_directory']['lat'] = pd.to_numeric(data['hs_directory']['lat'],errors = 'coerce')
data['hs_directory']['lon'] = pd.to_numeric(data['hs_directory']['lon'],errors = 'coerce')
