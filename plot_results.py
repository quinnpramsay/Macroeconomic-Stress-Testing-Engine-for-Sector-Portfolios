import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def summarize(pred: pd.DataFrame, name: str):
    cum_log = pred.sum(axis=0)
    cum_simple = np.exp(cum_log) - 1
    return pd.DataFrame({
        "scenario": name,
        "cum_12m_return": cum_simple
    }).sort_values("cum_12m_return")

def portfolio_path(pred: pd.DataFrame, weights: pd.Series):
    w = weights.reindex(pred.columns).fillna(0)
    port_log = pred.mul(w, axis=1).sum(axis=1)
    return np.exp(port_log.cumsum()) - 1

def sector_12m_returns(pred_df: pd.DataFrame):
    cum_log = pred_df.sum(axis=0)
    cum_simple = np.exp(cum_log) - 1
    return cum_simple.sort_values()

def plot_portfolio_paths(paths: dict):
    plt.figure()
    for name, series in paths.items():
        plt.plot(series.index, series.values, label=name)
    plt.axhline(0, linewidth=1)
    plt.title("Portfolio Cumulative Return Under Scenarios")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_sector_bars(sector_returns: pd.Series, title: str):
    plt.figure(figsize=(9, 4))
    plt.bar(sector_returns.index, sector_returns.values)
    plt.axhline(0, linewidth=1)
    plt.title(title)
    plt.xlabel("Sector ETF")
    plt.ylabel("12-Month Return")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, axis="y", alpha=0.3)
    plt.show()
