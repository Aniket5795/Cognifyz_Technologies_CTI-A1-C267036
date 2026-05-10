import pandas as pd

#-----------LOAD DATASET-------------
df = pd.read_csv("Dataset.csv")

#----------COUNTING RESTAURANT CHAINS-----------
chains = df['Restaurant Name'].value_counts()
restaurant_chains = chains[chains > 1]

#---------ANALYZING RATING AND POPULARITY------------
chain_analysis = (df[df['Restaurant Name'].isin(restaurant_chains.index)].groupby('Restaurant Name').agg(Number_of_Outlets=('Restaurant Name', 'count'), Average_Rating=('Aggregate rating', 'mean'), Average_Votes=('Votes', 'mean')).sort_values(by='Number_of_Outlets', ascending=False))

#------------------RESULT-------------------
print(f"Restaurant Chains:\n{restaurant_chains}\n\nChain Analysis (Ratings and Popularity):\n{chain_analysis}")