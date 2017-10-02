## 3. Condensing the Class Size Data Set ##

class_size =  data['class_size']
class_size = class_size[class_size['GRADE '] == '09-12']
class_size = class_size[class_size['PROGRAM TYPE'] == 'GEN ED']
class_size.head()

## 5. Computing Average Class Sizes ##

import numpy
group = class_size.groupby("DBN")
class_size = group.agg(numpy.mean)
class_size.reset_index(inplace=True)
data['class_size'] = class_size
data['class_size'].head()


## 7. Condensing the Demographics Data Set ##

data['demographics']=data['demographics'][data['demographics']['schoolyear'] == 20112012]
data['demographics'].head()

## 9. Condensing the Graduation Data Set ##

data['graduation'] = data['graduation'][data['graduation']['Cohort'] == '2006']
data['graduation'] = data['graduation'][data['graduation']['Demographic'] == 'Total Cohort']
data['graduation'].head()


                                                         

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
ap = data['ap_2010']
for each in cols:
    ap[each] = pd.to_numeric(ap[each],errors='coerce')
    
ap.head()

## 12. Performing the Left Joins ##

combined = data["sat_results"]
combined = combined.merge(data['ap_2010'],how='left',on='DBN')
combined = combined.merge(data['graduation'],how='left',on='DBN')
combined.shape

## 13. Performing the Inner Joins ##

cols = ['class_size','demographics','survey','hs_directory']
for each in cols:
    combined = combined.merge(data[each],how='inner',on='DBN')

combined.shape

## 15. Filling in Missing Values ##

combined = combined.fillna(combined.mean())
combined = combined.fillna(0)
combined.head()

## 16. Adding a School District Column for Mapping ##

def first_two(string):
    first_two = string[0:2]
    return first_two

combined['school_dist'] = combined['DBN'].apply(first_two)
combined['school_dist'].head()
    