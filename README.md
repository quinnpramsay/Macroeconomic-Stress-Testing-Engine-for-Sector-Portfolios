# Checklist
1. Setup

 Define project scope (sector portfolio stress testing)

 Create project folder structure

 Set up Colab / Jupyter environment

 Create .gitignore and requirements.txt

2. Data Ingestion

 Get and store FRED API key securely

 Download macroeconomic data (FRED)

 Download sector ETF price data

 Save raw data files (parquet)

 Verify date ranges and frequencies

Outputs:

macro_raw.parquet

sector_prices_raw.parquet

3. Data Processing

 Transform macro variables (YoY %, differences)

 Convert prices to monthly log returns

 Align macro and market data (monthly)

 Handle missing values

 Save processed datasets

Outputs:

macro_features.parquet

sector_returns.parquet

4. Feature Engineering

 Create lagged macro features (1, 3, 6, 12 months)

 Build model-ready dataset (date × sector)

 Check for data leakage and sanity-check features

Output:

model_dataset.parquet

5. Modeling

 Train distributed-lag regression models by sector

 Evaluate out-of-sample performance

 Implement Ridge/Lasso for robustness

 Compare and select final models

6. Scenario Engine

 Define standard macro scenarios (recession, rate shock, etc.)

 Implement historical replay scenarios

 Implement user-defined shock scenarios

 Project sector returns under each scenario

7. Portfolio & Risk Analysis

 Allow user-defined sector weights

 Aggregate sector returns to portfolio level

 Compute expected returns and downside risk

 Attribute risk to macro drivers

8. Visualization

 Build dashboard (Streamlit or equivalent)

 Scenario comparison views

 Sector sensitivity heatmaps

 Portfolio impact summaries

9. Finalization

 Refactor logic into /src modules

 Clean and organize notebooks

 Write README (problem, approach, results)

 Document assumptions and limitations

 Push clean repo to GitHub

# Instructions

To get the FRED data, first you have to:
pip install fredapi
