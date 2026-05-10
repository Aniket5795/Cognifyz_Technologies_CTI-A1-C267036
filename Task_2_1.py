import pandas as pd
import matplotlib.pyplot as plt

#---------LOAD DATASET----------
df = pd.read_csv("Dataset.csv")

#---------------PLOTTING------------------
plt.figure()
plt.hist(df['Aggregate rating'].dropna(), bins=10)
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Aggregate Ratings")
plt.show()

#---------COMMON RATING RANGE------------
rating_bins = pd.cut(df['Aggregate rating'], bins=10)
most_common_range = rating_bins.value_counts().idxmax()

#-----------AVERAGE NUMBER OF VOTES-------------
average_votes = df['Votes'].mean()

#-----------------RESULTS--------------------
print(f"Most common rating range: {most_common_range}\nAverage number of votes: {average_votes}")