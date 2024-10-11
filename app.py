import pandas as pd

# Load the dataset (replace with your actual path if needed)
file_path = 'product_amz.csv'
df = pd.read_csv(file_path)

# Define weights for each factor
weight_bsr = 0.4
weight_ratings = 0.3
weight_sold = 0.3

# Convert necessary columns to numeric types
df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce')
df['no_of_ratings'] = pd.to_numeric(df['no_of_ratings'].str.replace(',', ''), errors='coerce')
df['sold_in_last_month'] = pd.to_numeric(df['sold_in_last_month'], errors='coerce')
df['BSR_classificationRanks_rank'] = pd.to_numeric(df['BSR_classificationRanks_rank'], errors='coerce')

# Invert BSR because a lower rank is better
df['BSR_inverted'] = df['BSR_classificationRanks_rank'].max() - df['BSR_classificationRanks_rank']

# Calculate the weighted score (no normalization)
df['score'] = (weight_bsr * df['BSR_inverted']) + (weight_ratings * df['ratings']) + (weight_sold * df['sold_in_last_month'])

# Sort by the score in descending order and get the top 5
top5_recommendations = df.sort_values(by='score', ascending=False).head(5)

# Select relevant columns to display
top5_recommendations = top5_recommendations[['name', 'ratings', 'sold_in_last_month', 'BSR_classificationRanks_rank', 'score']]

print(top5_recommendations)
