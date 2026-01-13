from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import Ridge
import numpy as np

def ts_cv_r2(X, y, alpha=10.0, splits=5):
    tscv = TimeSeriesSplit(n_splits=splits)
    scores = []

    for train_idx, test_idx in tscv.split(X):
        model = Ridge(alpha=alpha)
        model.fit(X.iloc[train_idx], y.iloc[train_idx])
        scores.append(model.score(X.iloc[test_idx], y.iloc[test_idx]))

    return float(np.mean(scores))
