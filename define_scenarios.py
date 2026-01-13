import pandas as pd

def make_scenario(base: pd.DataFrame, name: str):
    sc = base.copy()
    sc.attrs["name"] = name
    return sc

def define_scenarios(baseline_path: pd.DataFrame):
    rate_shock = make_scenario(baseline_path, "Rate Shock")
    rate_shock.loc[rate_shock.index[:6], "fed_funds_change"] += 1.00 / 6

    recession = make_scenario(baseline_path, "Recession")
    recession["unemployment_change"] += 0.10
    recession["industrial_prod_yoy"] += -0.02
    recession["yield_spread"] += -0.75

    stagflation = make_scenario(baseline_path, "Stagflation")
    stagflation["cpi_yoy"] += 0.02
    stagflation["industrial_prod_yoy"] += -0.015
    stagflation["yield_spread"] += -0.25

    return rate_shock, recession, stagflation
