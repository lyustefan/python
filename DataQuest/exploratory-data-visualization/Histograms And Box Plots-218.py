## 2. Frequency Distribution ##

fandango_distribution = norm_reviews["Fandango_Ratingvalue"].value_counts().sort_index()
imdb_distribution = norm_reviews["IMDB_norm"].value_counts().sort_index()
print(fandango_distribution)
print(imdb_distribution)

## 4. Histogram In Matplotlib ##

fig, ax = plt.subplots()
ax.hist(norm_reviews["Fandango_Ratingvalue"],range=(0,5))
plt.show()

## 5. Comparing histograms ##

fig = plt.figure(figsize=(10,40))

cols = ["Fandango_Ratingvalue","RT_user_norm","Metacritic_user_nom","IMDB_norm"]
title_name = ["Distribution of Fandango Ratings","Distribution of Rotten Tomatoes Ratings","Distribution of Metacritic Ratings","Distribution of IMDB Ratings"]

for i in range(4):
    ax = fig.add_subplot(4,1,i+1)
    ax.hist(norm_reviews[cols[i]],bins = 20, range = (0,5))
    ax.set_title(title_name[i])
    ax.set_ylim(0,50)           

plt.show()

## 7. Box Plot ##

fig, ax = plt.subplots()
ax.boxplot(norm_reviews["RT_user_norm"])
ax.set_xticklabels(["Rotten Tomatoes"])
ax.set_ylim(0,5)
plt.show()


## 8. Multiple Box Plots ##

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
fig, ax = plt.subplots()
ax.boxplot(norm_reviews[num_cols].values)
ax.set_xticklabels(num_cols, rotation=90)
ax.set_ylim(0,5)
plt.show()