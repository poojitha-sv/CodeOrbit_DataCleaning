import pandas as pd

df = pd.read_csv("messy_customers.csv")
print("Original data shape:", df.shape)


df = df.drop_duplicates()
print("After removing exact duplicates:", df.shape)


df['Name'] = df['Name'].astype(str).str.strip()
df['Email'] = df['Email'].astype(str).str.strip()
df['City'] = df['City'].astype(str).str.strip()


df['Name'] = df['Name'].replace('nan', pd.NA)
df['Email'] = df['Email'].replace('nan', pd.NA)
df['City'] = df['City'].replace('nan', pd.NA)

df['Name'] = df['Name'].str.title()
df['City'] = df['City'].str.title()
df['Email'] = df['Email'].str.lower()

df = df.sort_values('PurchaseAmount', na_position='last')
df = df.drop_duplicates(subset='CustomerID', keep='first')
print("After removing the David Lee duplicate:", df.shape)


df['SignupDate'] = pd.to_datetime(df['SignupDate'], errors='coerce', format='mixed')
df['SignupDate'] = df['SignupDate'].dt.strftime('%Y-%m-%d')


df['Name'] = df['Name'].fillna('Unknown')
df['Phone'] = df['Phone'].fillna('Missing')
df['SignupDate'] = df['SignupDate'].fillna('Missing')


median_val = df['PurchaseAmount'].median()
df['PurchaseAmount'] = df['PurchaseAmount'].fillna(median_val)
print("Filled missing purchase amounts with median:", median_val)


df['CustomerID'] = df['CustomerID'].astype(int)
df['PurchaseAmount'] = df['PurchaseAmount'].round(2)


df = df.sort_values('CustomerID').reset_index(drop=True)
df.to_csv('cleaned_customers.csv', index=False)

print("\nDone! Final shape:", df.shape)
print(df)
