"""
data_prep.py
Utilities to clean and impute retail sales data.

Usage:
    python src/data_prep.py --input data/sample_retail_sales.csv --output data/cleaned_sample.csv
"""
import argparse
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer

def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    # Standardize numeric columns
    df = df.copy()
    # Convert UnitPrice to numeric (coerce errors)
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
    # Negative units or prices are invalid -> set to NaN for imputation
    df.loc[df["UnitsSold"] < 0, "UnitsSold"] = np.nan
    df.loc[df["UnitPrice"] <= 0, "UnitPrice"] = np.nan
    # TotalSales: if inconsistent (<=0) mark NaN; otherwise keep
    df.loc[df["TotalSales"] <= 0, "TotalSales"] = np.nan
    return df

def impute_simple(df: pd.DataFrame, numeric_cols):
    imputer = SimpleImputer(strategy="median")
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
    return df

def impute_iterative(df: pd.DataFrame, numeric_cols):
    imputer = IterativeImputer(random_state=0, max_iter=20)
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
    return df

def recompute_totals(df: pd.DataFrame):
    df = df.copy()
    df["TotalSales"] = df["UnitsSold"] * df["UnitPrice"]
    return df

def main(args):
    df = pd.read_csv(args.input)
    print(f"Loaded {len(df)} rows")
    df = basic_cleaning(df)
    numeric_cols = ["UnitsSold", "UnitPrice", "TotalSales"]
    if args.method == "simple":
        df = impute_simple(df, numeric_cols)
    else:
        df = impute_iterative(df, numeric_cols)
    # Recompute totals to ensure consistency
    df = recompute_totals(df)
    df.to_csv(args.output, index=False)
    print(f"Wrote cleaned data to {args.output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--method", choices=["simple","iterative"], default="iterative")
    args = parser.parse_args()
    main(args)
