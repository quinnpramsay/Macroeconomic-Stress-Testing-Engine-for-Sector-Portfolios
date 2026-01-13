# Introduction
This project looks at how different parts of the stock market respond to changes in the broader economy. Instead of trying to predict stock prices, the goal is to understand how economic factors like interest rates, inflation, unemployment, and overall economic growth affect different market sectors over time. Some sectors react immediately to economic shifts, while others respond more slowly or are more resilient. This project focuses on identifying those differences using historical data.

To do this, I analyzed changes in key macroeconomic indicators and measured how those changes impacted sector-level returns with time delays built in. I then tested several economic stress scenarios, including rapid interest rate increases, a recession, and stagflation, to see how each sector and a portfolio would be expected to perform under those conditions. The results highlight which sectors are most exposed to certain economic environments and which tend to hold up better. Overall, the project serves as a framework for understanding how economic stress moves through the market rather than a tool for short-term prediction.

# Instructions

To get the FRED data, first you have to:
"pip install fredapi" in the terminal

# ETF's

XLF — Financials
Banks, insurance companies, asset managers

XLK — Technology
Software, hardware, semiconductors

XLV — Healthcare
Pharma, biotech, healthcare services

XLY — Consumer Discretionary
Retail, autos, travel, luxury goods

XLP — Consumer Staples
Food, beverages, household products

XLE — Energy
Oil, gas, energy equipment

XLI — Industrials
Manufacturing, aerospace, logistics

XLB — Materials
Chemicals, metals, construction materials

XLU — Utilities
Electric, gas, and water utilities

XLRE — Real Estate
REITs and property-related firms. housing and financing driven
(Launched in 2015)

XLC — Communication Services
Media, telecom, internet platforms
(Launched in 2018)

# Macroeconomic Indicators
CPI — Inflation (CPIAUCSL)

Federal Funds Rate — Interest Rates (FEDFUNDS)

Unemployment Rate — Labor Market (UNRATE)

10Y–2Y Yield Spread — Yield Curve (T10Y2Y)

Industrial Production — Economic Activity (INDPRO)
