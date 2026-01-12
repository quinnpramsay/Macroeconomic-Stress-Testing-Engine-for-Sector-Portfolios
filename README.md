# Introduction
This project looks at how different parts of the stock market respond to changes in the broader economy. Instead of trying to predict stock prices, the goal is to understand how economic factors like interest rates, inflation, unemployment, and overall economic growth affect different market sectors over time. Some sectors react immediately to economic shifts, while others respond more slowly or are more resilient. This project focuses on identifying those differences using historical data.

To do this, I analyzed changes in key macroeconomic indicators and measured how those changes impacted sector-level returns with time delays built in. I then tested several economic stress scenarios, including rapid interest rate increases, a recession, and stagflation, to see how each sector and a portfolio would be expected to perform under those conditions. The results highlight which sectors are most exposed to certain economic environments and which tend to hold up better. Overall, the project serves as a framework for understanding how economic stress moves through the market rather than a tool for short-term prediction.

# Instructions

To get the FRED data, first you have to:
"pip install fredapi" in the terminal

# ETF's

XLF — Financials
Banks, insurance companies, asset managers
Very sensitive to interest rates and yield curves

XLK — Technology
Software, hardware, semiconductors
Sensitive to rates, growth expectations, valuations

XLV — Healthcare
Pharma, biotech, healthcare services
More defensive; less cyclical

XLY — Consumer Discretionary
Retail, autos, travel, luxury goods
Strongly tied to economic growth and employment

XLP — Consumer Staples
Food, beverages, household products
Defensive; holds up in recessions

XLE — Energy
Oil, gas, energy equipment
Driven by inflation, commodities, geopolitics

XLI — Industrials
Manufacturing, aerospace, logistics
Sensitive to economic cycles and production

XLB — Materials
Chemicals, metals, construction materials
Linked to inflation and global demand

XLU — Utilities
Electric, gas, water utilities
Bond-like; sensitive to interest rates

XLRE — Real Estate
REITs and property-related firms
Very rate-sensitive; housing and financing driven
(Launched in 2015)

XLC — Communication Services
Media, telecom, internet platforms (e.g., Meta, Google)
Growth-oriented, advertising-driven
(Launched in 2018)

# Macroeconomic Indicators

CPI — Inflation (CPIAUCSL)
Measures changes in consumer prices
Captures inflation pressure on costs, margins, and purchasing power

Federal Funds Rate — Interest Rates (FEDFUNDS)
Benchmark short-term interest rate set by the Fed
Drives borrowing costs, valuations, and financial conditions

Unemployment Rate — Labor Market (UNRATE)
The percentage of the labor force that is unemployed
Signals economic strength, consumer demand, and recession risk

10Y–2Y Yield Spread — Yield Curve (T10Y2Y)
Difference between long-term and short-term Treasury yields
Common recession indicator; inversions often precede downturns

Industrial Production — Economic Activity (INDPRO)
Measures output of factories, mines, and utilities
Reflects real economic growth and business cycle momentum
