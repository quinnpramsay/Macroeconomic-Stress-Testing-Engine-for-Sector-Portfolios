import pandas as pd
import yfinance as yf
from fredapi import Fred
from google.colab import userdata

FRED_API_KEY = userdata.get("FRED_API_KEY")
fred = Fred(api_key=FRED_API_KEY)

SERIES = {
    "cpi": "CPIAUCSL",
    "fed_funds": "FEDFUNDS",
    "unemployment": "UNRATE",
    "yield_spread": "T10Y2Y",
    "industrial_production": "INDPRO"
}

TICKERS = [
    "XLF","XLK","XLV","XLY","XLP","XLE",
    "XLI","XLB","XLU","XLRE","XLC"
]

def fetch_macro_data():
    macro = pd.DataFrame({name: fred.get_series(code) for name, code in SERIES.items()})
    macro = macro.resample("ME").last()
    macro = macro.loc["2000-01-31":].dropna()
    return macro

def fetch_sector_prices():
    prices = yf.download(TICKERS, start="2000-01-01", auto_adjust=True)["Close"]
    monthly_prices = prices.resample("ME").last()
    returns = monthly_prices.pct_change().apply(lambda x: np.log(1 + x))
    return returns.dropna(how="all")
