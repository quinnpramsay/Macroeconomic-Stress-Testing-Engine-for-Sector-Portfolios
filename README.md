# Introduction
At its core, this project is about understanding how different parts of the stock market respond to changes in the economy over time. The goal is not to predict stock prices, but to see how major economic forces like interest rates, inflation, unemployment, and economic slowdowns affect different sectors in different ways. Some industries react quickly to economic changes, while others respond months later or are more resilient overall. This project is meant to capture those differences and explain them using real historical data.

To do this, I treated the economy as a set of macroeconomic signals and the stock market as a group of broad sectors such as financials, technology, energy, and utilities. Instead of using the raw levels of economic data, I focused on how those values change, since markets usually react more to changes than to absolute numbers. I also added time lags to the data to reflect the idea that economic shocks do not affect every sector immediately. This allows the analysis to capture delayed effects, like how interest rate changes might impact technology months later or how a weakening labor market slowly affects consumer focused industries.

After estimating these relationships, I used them to run stress tests, which is the main purpose of the project. Rather than asking what will happen next month, I tested what would happen if the economy entered specific negative scenarios such as rapid interest rate hikes, a recession, or stagflation. I applied these shocks to the economic variables and used the model to estimate how each sector and a portfolio would respond over the following year. The focus is on relative risk, not exact outcomes. The project helps explain which sectors are more vulnerable under different economic conditions and how economic stress spreads through the market over time.


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
