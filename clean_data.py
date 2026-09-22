import pandas as pd

# loading the messy dataset
df = pd.read_csv("messy_customers.csv")
print("Original data shape:", df.shape)

# 1. removing duplicate rows
df = df.drop_duplicates()
print("After removing exact duplicates:", df.shape)

# 2. removing extra spaces from text columns
df['Name'] = df['Name'].astype(str).str.strip()
df['Email'] = df['Email'].astype(str).str.strip()
df['City'] = df['City'].astype(str).str.strip()

# fixing the "nan" strings that show up after using astype(str)
df['Name'] = df['Name'].replace('nan', pd.NA)
df['Email'] = df['Email'].replace('nan', pd.NA)
df['City'] = df['City'].replace('nan', pd.NA)

# 3. fixing capitalization
df['Name'] = df['Name'].str.title()
df['City'] = df['City'].str.title()
df['Email'] = df['Email'].str.lower()

# 4. found that customer 9 (David Lee) was entered twice, one row was
# missing the purchase amount. keeping the row that has the amount filled in
df = df.sort_values('PurchaseAmount', na_position='last')
df = df.drop_duplicates(subset='CustomerID', keep='first')
print("After removing the David Lee duplicate:", df.shape)

# 5. dates were in different formats so converting all to one format
df['SignupDate'] = pd.to_datetime(df['SignupDate'], errors='coerce', format='mixed')
df['SignupDate'] = df['SignupDate'].dt.strftime('%Y-%m-%d')

# 6. filling missing values
df['Name'] = df['Name'].fillna('Unknown')
df['Phone'] = df['Phone'].fillna('Missing')
df['SignupDate'] = df['SignupDate'].fillna('Missing')

# for purchase amount, using median since it's a number column
median_val = df['PurchaseAmount'].median()
df['PurchaseAmount'] = df['PurchaseAmount'].fillna(median_val)
print("Filled missing purchase amounts with median:", median_val)

# 7. fixing data types
df['CustomerID'] = df['CustomerID'].astype(int)
df['PurchaseAmount'] = df['PurchaseAmount'].round(2)

# sorting by customer id and saving
df = df.sort_values('CustomerID').reset_index(drop=True)
df.to_csv('cleaned_customers.csv', index=False)

print("\nDone! Final shape:", df.shape)
print(df)
