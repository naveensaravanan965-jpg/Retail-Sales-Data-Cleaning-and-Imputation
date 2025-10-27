# Retail Sales Data Cleaning and Imputation

**Project name:** Retail Sales Data Cleaning and Imputation  
**SDG:** SDG 8 — Decent Work and Economic Growth (handle missing/inconsistent retail sales data for reliable analysis)

## Goal
Provide a reproducible mini-project that demonstrates:
- loading retail sales data,
- cleaning inconsistent entries,
- handling missing values (imputation with different strategies),
- simple exploratory plots,
- producing a clean dataset ready for analysis or forecasting.

## Structure
```
Retail_Sales_Data_Cleaning_and_Imputation/
├─ data/
│  └─ sample_retail_sales.csv
├─ src/
│  ├─ data_prep.py        # core cleaning + imputation functions + CLI
│  └─ visualize.py        # quick plotting utilities
├─ notebooks/
│  └─ example_usage.py    # script-style notebook example
├─ requirements.txt
├─ .gitignore
└─ README.md
```

## How to run
1. Create virtualenv and install requirements:
```bash
python -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Clean and impute:
```bash
python src/data_prep.py --input data/sample_retail_sales.csv --output data/cleaned_sample.csv
```

3. Visualize:
```bash
python src/visualize.py --input data/cleaned_sample.csv
```

## Notes
- This project includes a small synthetic sample dataset to test the pipeline.
- The `data_prep.py` script demonstrates conservative cleaning rules (e.g., remove or correct negative values) and two imputation strategies (median, IterativeImputer).
