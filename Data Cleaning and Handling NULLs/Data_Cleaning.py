import pandas as pd
import numpy as np

data = {
    'patient_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 101, 107, 118, 119, 120],
    'age': ['25', '34', None, '45', '29', None, '38', '52', '27', '41',
            '33', 'unknown', '48', '26', '35', '25', '38', '31', None, '44'],
    'weight': ['70', '65', '80', None, '75', None, '68', '90', '72', '85',
               '78', None, '82', '69', 'N/A', '70', '68', '74', None, '88'],
    'blood_pressure': [120, 130, None, 140, 125, None, 135, None, 118, 145,
                      128, None, 138, 122, None, 120, 135, 126, None, 142],
    'medication': ['Aspirin', 'Metformin', 'Lisinopril', None, 'Aspirin',
                   'Metformin', 'Lisinopril', 'Aspirin', None, 'Metformin',
                   'Lisinopril', 'Aspirin', None, 'Metformin', 'Aspirin',
                   'Aspirin', 'Lisinopril', 'Metformin', 'Aspirin', None],
    'insurance_provider': ['Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None,
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', 'Blue Cross',
                          'Aetna', None, 'UnitedHealth', 'Blue Cross', 'Aetna',
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None]
}

df = pd.DataFrame(data)
"""
print(df)

# Task 1: Inspect the Data
# Use df.info() to view column data types and non-null counts
print(df.info())

# Use df.isnull().sum() to count missing values per column
print(df.isnull().sum())


# Calculate the percentage of missing values using: (df.isnull().sum() / len(df)) * 100
# print(df.isnull().sum()/df.shape[0]*100)
print(df.isnull().sum()/len(df)*100)


# Use df.duplicated().sum() to count duplicate rows
# print(df[df.duplicated()])
print(df.duplicated().sum())


# Task 2: Data Type Conversion
# Convert age column to numeric using pd.to_numeric(df['age'], errors='coerce')
df_copy = df.copy()
df_copy["age"] = pd.to_numeric(df_copy["age"], errors='coerce')

# Convert weight column to numeric using pd.to_numeric(df['weight'], errors='coerce')
df_copy["weight"]= pd.to_numeric(df_copy["weight"], errors= 'coerce')
print(df_copy.dtypes)

# Check how many NEW missing values were created after conversion
print(df_copy.isnull().sum())


# Convert insurance_provider to category type using astype('category')
print(df_copy.dtypes)
df_copy['insurance_provider'] = df_copy['insurance_provider'].astype('category')

# Use df.dtypes to verify all conversions
print(df_copy.dtypes)

# Task 3: Handle Missing Values
# Apply appropriate strategies for each column:
# age: Fill with median using fillna(df['age'].median())
age_median = df_copy["age"].median()
print(f"The mean of age is {age_median}")
df_copy["age"] = df_copy['age'].fillna(age_median)


# weight: Fill with median using fillna(df['weight'].median())
weight_median = df_copy["weight"].median()
print(f"The median of weight is {weight_median}")
df_copy["weight"] = df_copy["weight"].fillna(weight_median)


# blood_pressure: Fill with median using fillna(df['blood_pressure'].median())
bp_median = df_copy["blood_pressure"].median()
df_copy["blood_pressure"] = df_copy['blood_pressure'].fillna(bp_median)


# medication: Fill with mode using fillna(df['medication'].mode()[0])
medication_mode = df_copy["medication"].mode()[0]
print(f"The first mode: {medication_mode}")
df_copy["medication"] = df_copy['medication'].fillna(medication_mode)


# insurance_provider: Fill with constant value 'Unknown'
# Since insurance provider is already type cast to category. Add all insurance provider values into category then fill
df_copy["insurance_provider"] = df_copy["insurance_provider"].cat.add_categories("Unknown").fillna("Unknown")
print(df_copy)

# Verify no missing values remain using df.isnull().sum()
print(df_copy.isnull().sum())


# Task 4: Handle Duplicates
# View duplicate rows using df[df.duplicated(keep=False)]
print(df[df.duplicated(keep=False)])

# Identify duplicates based on patient_id only using df.duplicated(subset=['patient_id'])
print(df_copy[df_copy.duplicated(subset=["patient_id"])])


# Remove duplicates keeping first occurrence: df.drop_duplicates(subset=['patient_id'], keep='first')
# Print shape before and after to show how many rows were removed
print(df_copy.shape)
print(df_copy.drop_duplicates(subset=['patient_id'],keep="first"))
print(df_copy.shape)


# Task 5: Complete Workflow with Verification
# Start fresh: reload the DataFrame and create a copy using df_clean = df.copy()
# Perform ALL cleaning steps in order: types → missing values → duplicates
# Create a verification report showing:
# Shape before and after
# Missing values before and after
# Duplicates before and after
# Data types before and after
"""
df_clean = df.copy()
print("===========================Verification Report===========================")
print(f"\nShape of df before Cleaning:\n{df_clean.shape}")
print(f"\nData type of df before Cleaning:\n{df_clean.dtypes} ")
print(f"\nMissing Values before Cleaning:\n{df_clean.isnull().sum()}")
print(f"\nDuplicates before Cleaning:\n{df_clean.duplicated().sum()}")
print(f"Duplicated Rows:\n{df_clean[df_clean.duplicated(keep=False)]}\n")

# Fill None value of Age column with Median 
# Convert str type into numeric and apply median
df_clean["age"] = pd.to_numeric(df_clean["age"], errors='coerce')
age_median = df_clean["age"].median()
print(f"The mean of age is {age_median}")
df_clean["age"] = df_clean['age'].fillna(age_median)

# Fill None value of Weight column with Median
# Convert str type into numeric and apply median
df_clean["weight"] = pd.to_numeric(df_clean["weight"], errors='coerce')
weight_median = df_clean["weight"].median()
print(f"The median of weight is {weight_median}")
df_clean["weight"] = df_clean["weight"].fillna(weight_median)

# Fill None value of BP column with Median
bp_median = df_clean["blood_pressure"].median()
df_clean["blood_pressure"] = df_clean['blood_pressure'].fillna(bp_median)

# Fill None value of Medication column with Mode
medication_mode = df_clean["medication"].mode()[0]
print(f"The first mode: {medication_mode}")
df_clean["medication"] = df_clean['medication'].fillna(medication_mode)

# Fill None value of Insurance Provider column with Mode
ip_mode = df_clean["insurance_provider"].mode()[0]
print(f"The first mode: {ip_mode}")
df_clean["insurance_provider"] = df_clean["insurance_provider"].fillna(ip_mode)

# Drop duplicates
df_clean = df_clean.drop_duplicates(keep="first")

print(f"\nShape of df after Cleaning:\n{df_clean.shape}")
print(f"\nData type of df after Cleaning:\n{df_clean.dtypes}")
print(f"\nMissing Values after Cleaning:\n{df_clean.isnull().sum()}")
print(f"\nDuplicates after Cleaning:\n{df_clean.duplicated().sum()}")
print(f"Duplicated Rows:\n{df_clean[df_clean.duplicated(keep=False)]}\n")

