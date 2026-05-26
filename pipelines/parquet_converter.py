import pandas as pd



df = pd.read_csv(
    "data/processed/cleaned_walmart.csv"
)



df.to_parquet(
    "data/curated/curated_walmart.parquet"
)


print("Parquet file created successfully!")