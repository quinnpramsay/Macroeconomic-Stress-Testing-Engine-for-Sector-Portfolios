# Description

This project builds a tool that shows how big economic changes—like interest rate hikes, inflation, or rising unemployment—affect different parts of the stock market. You use real economic data and sector ETFs (like tech, finance, energy) to measure how each sector historically responds to those changes, often with delays. Then you simulate “what-if” scenarios, such as a recession or rapid rate hikes, to estimate how each sector and a whole portfolio might perform. The output is a clear, decision-focused view of risk and downside, not stock price predictions. In simple terms, it answers: “If the economy moves this way, what happens to my portfolio?”

# Instructions

To get the FRED data, first you have to:
pip install fredapi

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
