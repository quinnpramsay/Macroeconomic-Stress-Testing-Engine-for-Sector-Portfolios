from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
import pandas as pd
import numpy as np
from utils.helpers import ts_cv_r2  # or define locally if not importing

def train_ridge_models(dataset, feature_cols, alpha=10.0):
    results = []
    coefficients = {}
    models = {}

    for sector in sorted(dataset["sector"].unique()):
        df = dataset[dataset["sector"] == sector].sort_values("Date")
        X = df[feature_cols]
        y = df["return"]

        cv_r2 = ts_cv_r2(X, y, alpha)
        pipe = Pipeline([("scaler", StandardScaler()), ("ridge", Ridge(alpha=alpha))])
        pipe.fit(X, y)

        models[sector] = pipe
        coefs = pd.Series(pipe.named_steps["ridge"].coef_, index=feature_cols)
        coefficients[sector] = coefs.sort_values(key=np.abs, ascending=False)

        results.append({
            "sector": sector,
            "observations": len(df),
            "cv_r2": cv_r2
        })

    return pd.DataFrame(results).sort_values("cv_r2", ascending=False), coefficients, models
