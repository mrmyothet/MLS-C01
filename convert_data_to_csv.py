import pandas as pd

# Step 1: Load the .data file
df = pd.read_csv('./census_income/adult.data', header=None)  # Add delimiter=',' if needed

# Step 2: Optionally assign column names
df.columns = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'
]

# Step 3: Save as CSV
df.to_csv('./census_income/adult.csv', index=False)