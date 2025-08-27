import pandas as pd
import kagglehub
import matplotlib.pyplot as plt

# --- 1. Data Ingestion ---
# Download the dataset using kagglehub
path = kagglehub.dataset_download(
    "ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training",
    path="dirty_cafe_sales.csv"
)
df = pd.read_csv(path)
print("Dataset loaded successfully.")

# --- 2. Initial Data Inspection ---
print("--- Initial Data Inspection ---")
print("First 5 rows:")
print(df.head())      ## with the head method, there are 8 columns
print("\nDataFrame Info:")
df.info()             ## .info() shows 8 different objects used in the dataframe, all the data shows some missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum()) ## Most missing values exist in the payment method and location columns
print("\nColumn names:")
print(df.columns)

# --- 3. Data Cleaning and Manipulation ---
print("\n--- Data Cleaning and Manipulation ---")

# Convert specific columns to numeric, coercing errors to NaN
columns_to_convert = ['Total Spent', 'Price Per Unit', 'Quantity']
df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')

# Drop rows where 'Item' is missing, as it's a critical identifier.
# We also drop rows with no 'Transaction Date' because they can't be reliably used.
df.dropna(subset=['Item', 'Transaction Date'], inplace=True)
print("\nMissing values after dropping rows with missing 'Item' or 'Transaction Date':")
print(df.isnull().sum())

# Impute missing values for 'Quantity' and 'Price Per Unit' using the mean.
df['Quantity'] = df['Quantity'].fillna(round(df['Quantity'].mean()))
df['Price Per Unit'] = df['Price Per Unit'].fillna(round(df['Price Per Unit'].mean(), 2))
print("\nMissing values after imputing 'Quantity' and 'Price Per Unit':")
print(df.isnull().sum())

# Calculate 'Total Spent' for rows where it is missing, but other necessary data is present.
mask_total_spent_missing = df['Total Spent'].isnull()
df.loc[mask_total_spent_missing, 'Total Spent'] = df['Price Per Unit'] * df['Quantity']
print("\nMissing values after calculating 'Total Spent':")
print(df.isnull().sum())

# Clean and fill 'Payment Method' column.
df['Payment Method'] = df['Payment Method'].replace(['ERROR', 'UNKNOWN'], 'Digital Wallet')
df['Payment Method'] = df['Payment Method'].fillna(df['Payment Method'].mode()[0])
print("\n'Payment Method' value counts after cleaning:")
print(df['Payment Method'].value_counts())

# Clean and fill 'Location' column.
# Based on my vast Restaurant experience in different roles, I can assume In-store as their designation
df['Location'] = df['Location'].replace(['ERROR', 'UNKNOWN'], 'In-store')
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])
print("\n'Location' value counts after cleaning:")
print(df['Location'].value_counts())

# Drop duplicate rows.
df.drop_duplicates(inplace=True)
print(f"\nNumber of duplicate rows found and dropped: {df.duplicated().sum()}")
# None Found

print("\n--- Final Data Check ---")
print("First 5 rows of the cleaned DataFrame:")
print(df.head())
print("\nFinal missing values check:")
print(df.isnull().sum())
print("\nData types of key columns:")
print(df[['Total Spent', 'Price Per Unit', 'Quantity']].dtypes)

# --- 3.1 Save Cleaned DataFrame to a CSV file ---
df.to_csv('cleaned_cafe_sales.csv', index=False)  ## index param tells pandas not to add an extra columns with indices

# --- 4. Data Visualization ---
print("\n--- Data Visualization ---")

# Payment method distribution chart
plt.figure()
df['Payment Method'].value_counts().plot(kind='bar')
plt.title('Frequency of Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# Location-type pie chart
plt.figure()
df['Location'].value_counts().plot(kind='pie')
plt.title('Distribution Location type')
plt.xlabel('Type of order')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# Histogram of Total Spent
plt.figure()
df['Total Spent'].plot(kind='hist', bins=30)
plt.title('Distribution of Total Spent in 30 subsets')
plt.xlabel('Total Spent')
plt.ylabel('Frequency')
plt.show()