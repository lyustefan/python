## 2. Array Comparisons ##

countries_canada = world_alcohol[:,2] == "Canada"
years_1984 = world_alcohol[:,0] == "1984"

## 3. Selecting Elements ##

country_is_algeria = (world_alcohol[:,2] == "Algeria")
country_algeria = world_alcohol[country_is_algeria, :]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Algeria")
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]
rows_with_algeria_and_1986

## 5. Replacing Values ##

is_1986 = world_alcohol[:,0] == "1986"
world_alcohol[is_1986,0] = "2014"
is_grog = world_alcohol[:,3] == "Wine"
world_alcohol[is_grog,3] = "Grog"

## 6. Replacing Empty Strings ##

is_value_empty = world_alcohol[:,4] == ""
world_alcohol[is_value_empty,4] = "0"

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

is_canada_1986 = (world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == "1986")
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = canada_1986[:,4]
empty = canada_alcohol == ""
canada_alcohol[empty] = "0"
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()



## 10. Calculating Consumption for Each Country ##

totals = {}
year = world_alcohol[world_alcohol[:,0] == "1989",:]
for each in countries:
    country_true = each == year[:,2]
    country_consumption = year[country_true,:]
    consumption_value = country_consumption[:,4]
    empty = consumption_value == ""
    consumption_value[empty] = "0"
    consumption_value = consumption_value.astype(float)
    totals[each] = consumption_value.sum()

    

    
    
    

    

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None

for k,v in totals.items():
    if v > highest_value:
        highest_value = v
        highest_key = k