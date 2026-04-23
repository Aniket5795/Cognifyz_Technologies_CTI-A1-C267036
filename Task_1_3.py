import pandas as pd
import matplotlib.pyplot as plt

#----LOAD DATASET------
df = pd.read_csv("Dataset .csv")

# -----COUNT RESTAURANTS IN EACH PRICE RANGE-------
price_counts = df['Price range'].value_counts().sort_index()

#------PERCENTAGE CALCULATIONS------
total_restaurants = len(df)
price_percentage = (price_counts/total_restaurants)*100

#----PLOT:-BAR CHART-----
plt.figure()
price_counts.plot(kind='bar')
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Price Ranges")
plt.show()

#------RESULT------
print(pd.DataFrame({'Price Range': price_counts.index, 'Count': price_counts.values, 'Percentage (%)': price_percentage.values}))