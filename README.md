# Introduction
At its core, this project is about understanding how different parts of the stock market react to changes in the economy over time, rather than trying to predict stock prices directly. The idea is that large macroeconomic forces—such as interest rate changes, inflation, labor market shifts, and recessions—don’t affect all industries equally or at the same speed. Some sectors react immediately, others respond months later, and some are more resilient overall. This project tries to measure those differences in a structured way using historical data.

To do that, I treated the economy as a set of macro signals (inflation, interest rates, unemployment, yield curve, and production) and the stock market as a set of economic sectors (financials, tech, energy, utilities, etc.). Instead of looking at the raw levels of these macro variables, I focused on changes in them—because markets care more about surprises and direction than absolute values. I also introduced time lags (1, 3, 6, and 12 months) to capture the idea that economic shocks don’t hit all sectors instantly. This allows the model to learn patterns such as “rate hikes hurt tech later” or “yield curve inversions damage financials after a delay.”

Once those relationships were estimated, I used them to run stress tests, which is really the heart of the project. Instead of asking “what will happen next month?”, I asked “what would happen if the economy moved in a specific bad direction?” I tested scenarios like rapid interest-rate hikes, a recession, and stagflation by manually applying economic shocks and seeing how each sector would be expected to respond over a year based on historical behavior. The goal wasn’t precision—it was relative risk. Which sectors get hit hardest? Which ones hold up better? And how does a portfolio behave under different macro environments? In the end, this project acts like a decision-support tool: it helps explain why certain sectors are risky in certain economic regimes and how macro conditions propagate through the market over time.


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
