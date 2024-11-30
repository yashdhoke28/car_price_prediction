import pandas as pd

# Load the dataset
df = pd.read_csv('CAR_DETAILS.csv')  # Update the file name if necessary
print("Dataset loaded successfully!")
print(df.head())  # Display the first few rows to understand the structure

# Check for missing values
print("Checking for missing values...")
print(df.isnull().sum())

# Fill missing values for numerical columns
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col].fillna(df[col].median(), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Save the cleaned dataset
df.to_csv('cleaned_car_details.csv', index=False)
print("Data cleaning complete! Cleaned dataset saved as 'cleaned_car_details.csv'.")
