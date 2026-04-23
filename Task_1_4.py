import pandas as pd

#----------LOAD DATASET-----------
df = pd.read_csv("Dataset.csv")

#--------PERCENTAGE OF RESTAURANTS OFFERING ONLINE DELIVERY---------
online_counts = df['Has Online delivery'].value_counts()
percentage = (online_counts/len(df))*100

#------------------AVERAGE RATINGS-----------------
avg_ratings = df.groupby('Has Online delivery')['Aggregate rating'].mean()

#----------------------RESULTS--------------------
print(f"Percentage of restaurants offering online delivery:\n{percentage}\n\nAverage ratings (Online Delivery vs Offline Delivery):\n{avg_ratings}")