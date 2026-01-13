import pandas as pd

def build_lagged_from_history_and_future(history: pd.DataFrame, future: pd.DataFrame, lags=[1, 3, 6, 12]):
    full = pd.concat([history, future], axis=0)
    parts = [full]
    for lag in lags:
        shifted = full.shift(lag)
        shifted.columns = [f"{c}_lag{lag}" for c in full.columns]
        parts.append(shifted)
    full_lagged = pd.concat(parts, axis=1)
    return full_lagged.loc[future.index].dropna()

def predict_scenario_returns(models, macro_history, scenario_df, feature_cols):
    X_future = build_lagged_from_history_and_future(macro_history, scenario_df)
    X_future = X_future[feature_cols]

    preds = pd.DataFrame(index=X_future.index)
    for sector, model in models.items():
        preds[sector] = model.predict(X_future)
    return preds
