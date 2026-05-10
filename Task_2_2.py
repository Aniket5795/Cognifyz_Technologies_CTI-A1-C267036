import pandas as pd

#---------LOAD DATASET----------
df = pd.read_csv("Dataset.csv")

#---------DROP MISSING CUISINES----------
df_cuisine = df.dropna(subset=['Cuisines'])

#---------MOST COMMON CUISINE COMBINATION----------
common_cuisine_combinations = df_cuisine['Cuisines'].value_counts().head(10)

#------------AVERAGE RATING-------------
avg_rating_combinations = df_cuisine.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)

#------------RESULTS--------------
print(f"Most common cuisine combinations:\n{common_cuisine_combinations}\n\nAverage ratings by cuisine combination:\n{avg_rating_combinations.head(10)}")