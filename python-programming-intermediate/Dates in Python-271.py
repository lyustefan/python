## 1. The Time Module ##

import time
current_time = time.time()
print(current_time)

## 2. Converting Timestamps ##

import time
current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour

## 3. UTC ##

import datetime
current_datetime = datetime.datetime.utcnow()
current_year = current_datetime.year
current_month = current_datetime.month

## 4. Timedelta ##

import datetime
kirks_birthday = datetime.datetime(year = 2233, month = 3, day = 22)
diff = datetime.timedelta( weeks = 15)
before_kirk = kirks_birthday - diff
print(kirks_birthday)


## 5. Formatting Dates ##

import datetime
mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print(mystery_date_formatted_string)                                                      

## 6. Parsing Dates ##

import datetime
mystery_date = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")
print(mystery_date)

## 8. Reformatting Our Data ##

import datetime
for each in posts:
    float_each = float(each[2])
    datetime_object = datetime.datetime.fromtimestamp(float_each)
    each[2] = datetime_object

## 9. Counting Posts from March ##

march_count = 0
for each in posts:
    if each[2].month == 3:
        march_count += 1

## 10. Counting Posts from Any Month ##


        
def post_count(input_month):
    march_count = 0
    for row in posts:
        if row[2].month == input_month:
            march_count += 1
    return march_count

feb_count = post_count(2)
aug_count = post_count(8)