import pandas as pd
import numpy as np

def create_macro_features(macro_df):
    features = pd.DataFrame(index=macro_df.index)
    features["cpi_yoy"] = macro_df["cpi"].pct_change(12)
    features["fed_funds_change"] = macro_df["fed_funds"].diff()
    features["unemployment_change"] = macro_df["unemployment"].diff()
    features["yield_spread"] = macro_df["yield_spread"]
    features["industrial_prod_yoy"] = macro_df["industrial_production"].pct_change(12)
    return features.dropna()

def add_lags(features, lags=[1, 3, 6, 12]):
    all_data = [features]
    for lag in lags:
        lagged = features.shift(lag)
        lagged.columns = [f"{col}_lag{lag}" for col in features.columns]
        all_data.append(lagged)
    return pd.concat(all_data, axis=1).dropna()
