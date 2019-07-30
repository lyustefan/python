## 3. Introduction To The Data ##

['import pandas as pd\nimport matplotlib.pyplot as plt\n\nwomen_degrees = pd.read_csv(\'percent-bachelors-degrees-women-usa.csv\')\n\nplt.plot(women_degrees["Year"],women_degrees["Biology"])\nplt.show()']

## 4. Visualizing The Gender Gap ##

plt.plot(women_degrees["Year"],women_degrees["Biology"], c = "blue", label = "Women")
plt.plot(women_degrees["Year"],100 - women_degrees["Biology"], c = "green", label = "Men")
plt.title("Percentage of Biology Degrees Awarded By Gender")
plt.legend(loc = "upper right")
plt.show()


## 6. Hiding Tick Marks ##

fig, ax = plt.subplots()
ax.plot(women_degrees["Year"],women_degrees["Biology"], c = "blue", label = "Women")
ax.plot(women_degrees["Year"],100 - women_degrees["Biology"], c = "green", label = "Men")

ax.tick_params(bottom="off",top="off",left="off",right="off")
plt.title("Percentage of Biology Degrees Awarded By Gender")
plt.legend(loc = "upper right")

print(ax.spines)

## 7. Hiding Spines ##

fig, ax = plt.subplots()
ax.plot(women_degrees['Year'], women_degrees['Biology'], label='Women')
ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], label='Men')
ax.tick_params(bottom="off", top="off", left="off", right="off")
ax.legend(loc='upper right')
ax.set_title('Percentage of Biology Degrees Awarded By Gender')
plt.show()

for key,spine in ax.spines.items():
    spine.set_visible(False)




## 8. Comparing Gender Gap Across Degree Categories ##

major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    # Remove all the spines from the plot
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    # Remove all the ticks from the plot
    ax.tick_params(top="off",bottom="off",left="off",right="off")
    ax.set_title(major_cats[sp])
# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()