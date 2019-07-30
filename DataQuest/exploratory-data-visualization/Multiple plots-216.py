## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
year_1948 = unrate[:12]
plt.plot(year_1948["DATE"],year_1948["VALUE"])
plt.xticks(rotation = 90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()

## 3. Matplotlib Classes ##

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

## 5. Adding Data ##

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(unrate[0:12]["DATE"],unrate[0:12]["VALUE"])
ax2.plot(unrate[12:24]["DATE"],unrate[12:24]["VALUE"])
plt.show()

## 6. Formatting And Spacing ##

fig = plt.figure(figsize = (12,6))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

## 7. Comparing Across More Years ##


ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

fig = plt.figure(figsize = (12,12))
for i in range(5):
    axes = fig.add_subplot(5,1,i+1)
    start_index = i * 12
    end_index = (i + 1) * 12
    subset = unrate[start_index:end_index]
    axes.plot(subset["DATE"],subset["VALUE"])

plt.show()
    
    

## 8. Overlaying Line Charts ##

unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize = (6,3))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c = "red")
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c = "blue")
plt.show()

## 9. Adding More Lines ##

fig = plt.figure(figsize = (10,6))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c = "red")
colors = ["red","blue","green","orange","black"]
for i in range(5):
    start_index = i * 12
    end_index = (i + 1) * 12
    plt.plot(unrate[start_index:end_index]["MONTH"],unrate[start_index:end_index]["VALUE"], c = colors[i])
    
plt.show()
    
           

## 10. Adding A Legend ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
labels = ['1948','1949', '1950', '1951', '1952']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=labels[i])
    
plt.legend(loc = 'upper left')
plt.show()

## 11. Final Tweaks ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')

plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.show()