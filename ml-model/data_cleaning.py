import pandas as pd


df = pd.read_csv("data/raw/Walmart_dataset.csv")


print("First 5 Rows:")
print(df.head())


print("\nDataset Info:")
print(df.info())


df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)


df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year


print("\nMissing Values:")
print(df.isnull().sum())


df.to_csv("data/processed/cleaned_walmart.csv", index=False)

print("\nDataset cleaned successfully!")