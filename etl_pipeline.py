import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Extract
df = pd.read_csv('sample_data.csv')
print("Original Data:")
print(df)

# Transform
# Handle missing values
imputer_num = SimpleImputer(strategy='mean')
df['Age'] = imputer_num.fit_transform(df[['Age']])
df['Salary'] = imputer_num.fit_transform(df[['Salary']])

# Encode categorical column
encoder = LabelEncoder()
df['Department'] = encoder.fit_transform(df['Department'])

# Scale numerical columns
scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

print("\nTransformed Data:")
print(df)

# Load
df.to_csv('processed_data.csv', index=False)
print("\nProcessed data saved to 'processed_data.csv'")
