#TASK: Top Cuisines
import pandas as pd

#Determine the top three mostcommon cuisines in the dataset

# -------LOAD DATASET--------
df = pd.read_csv("Dataset.csv")

# ------SPLIT CUISINES---------
cuisine = df['Cuisines'].dropna().str.split(',').explode()

#--------TOP 3 CUISINES----------
top_cuisines = cuisine.value_counts().head(3)

#Calculate the percentage ofrestaurants that serve each of the top cuisines

#-------PERCENTAGE CALCULATION---------
total_restaurants = len(df)
percentage = (top_cuisines / total_restaurants) * 100

#----------RESULT-----------
print(pd.DataFrame({'Cuisine': top_cuisines.index, 'Count': top_cuisines.values, 'Percentage (%)': percentage.values}))