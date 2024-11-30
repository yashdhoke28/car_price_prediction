import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('cleaned_car_details.csv')  # Ensure the correct path to your cleaned dataset
print("Dataset loaded for EDA!")
print(df.head())  # Display the first 5 rows to verify the dataset

# Plot the distribution of selling prices
plt.figure(figsize=(10, 6))
sns.histplot(df['selling_price'], kde=True, bins=30, color='blue')
plt.title('Distribution of Selling Prices')
plt.xlabel('Selling Price (in ₹)')
plt.ylabel('Frequency')
plt.savefig('selling_price_distribution.png')  # Save the plot as an image
plt.show()

# Scatter plot: km_driven vs selling_price
plt.figure(figsize=(10, 6))
sns.scatterplot(x='km_driven', y='selling_price', data=df, color='green')
plt.title('Scatter Plot: Km Driven vs Selling Price')
plt.xlabel('Kilometers Driven')
plt.ylabel('Selling Price (in ₹)')
plt.savefig('km_driven_vs_selling_price.png')  # Save the scatter plot as an image
plt.show()

# Select only numeric columns for correlation analysis
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# Plot a heatmap of feature correlations
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')  # Save the plot as an image
plt.show()
