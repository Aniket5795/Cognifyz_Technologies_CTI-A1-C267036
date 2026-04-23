import pandas as pd

#-------LOAD DATASET----------
df = pd.read_csv("Dataset.csv")

#------CITY WITH HIGHEST NUMBER OF RESTAURANTS------
city_counts = df['City'].value_counts()
top_city_by_count = city_counts.idxmax()

#-------AVERAGE RATING FOR EACH CITY--------
avg_rating_city = df.groupby('City')['Aggregate rating'].mean()

#------CITY WITH HIGHEST AVERAGE RATING--------
top_city_by_rating = avg_rating_city.idxmax()

print(f"City with highest number of restaurants:{top_city_by_count}\n\nAverage rating for each city:\n{avg_rating_city}\n\nCity with highest average rating:{top_city_by_rating}")