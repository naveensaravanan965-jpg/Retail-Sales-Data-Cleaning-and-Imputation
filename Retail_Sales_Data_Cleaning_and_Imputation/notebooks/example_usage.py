# Example usage script (can be opened as a notebook)
from pathlib import Path
import pandas as pd
from src.data_prep import basic_cleaning, impute_iterative, recompute_totals

df = pd.read_csv("data/sample_retail_sales.csv")
print("Before cleaning:")
print(df.head(10))

df_clean = basic_cleaning(df)
numeric_cols = ["UnitsSold", "UnitPrice", "TotalSales"]
df_clean = impute_iterative(df_clean, numeric_cols)
df_clean = recompute_totals(df_clean)

print("\nAfter cleaning + imputation:")
print(df_clean.head(10))
df_clean.to_csv("data/cleaned_sample.csv", index=False)
