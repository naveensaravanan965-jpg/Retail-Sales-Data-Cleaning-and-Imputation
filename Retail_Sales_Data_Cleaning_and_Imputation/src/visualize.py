"""
visualize.py
Simple plotting utilities for the cleaned dataset.
Usage:
    python src/visualize.py --input data/cleaned_sample.csv
"""
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def plot_units_by_store(df):
    grouped = df.groupby("StoreID")["UnitsSold"].sum()
    grouped.plot(kind="bar", title="Total Units Sold per Store")
    plt.tight_layout()
    plt.show()

def plot_sales_over_time(df):
    df["Date"] = pd.to_datetime(df["Date"])
    daily = df.groupby("Date")["TotalSales"].sum()
    daily.plot(title="Daily Total Sales")
    plt.tight_layout()
    plt.show()

def main(args):
    df = pd.read_csv(args.input)
    plot_units_by_store(df)
    plot_sales_over_time(df)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    main(args)
