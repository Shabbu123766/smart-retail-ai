import pandas as pd



# LOAD RAW DATA

df = pd.read_csv(
    "data/raw/walmart_dataset.csv"
)



# STAGED LAYER

# Remove null values
df = df.dropna()


# Remove duplicates
df = df.drop_duplicates()


# Save staged dataset
df.to_csv(
    "data/processed/cleaned_walmart.csv",
    index=False
)


print("Staged dataset created.")


# CURATED LAYER

curated_df = df[[
    "Store",
    "Weekly_Sales",
    "Holiday_Flag",
    "Temperature",
    "Fuel_Price",
    "CPI",
    "Unemployment"
]]


# Add business column
curated_df["Sales_Category"] = curated_df[
    "Weekly_Sales"
].apply(
    lambda x: "High" if x > 1000000 else "Low"
)


# Add profit estimate
curated_df["Profit_Estimate"] = (
    curated_df["Weekly_Sales"] * 0.15
)


# Save curated dataset
curated_df.to_csv(
    "data/curated/curated_walmart.csv",
    index=False
)


print("Curated dataset created.")