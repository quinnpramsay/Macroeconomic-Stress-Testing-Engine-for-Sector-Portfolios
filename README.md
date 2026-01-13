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

# Worst-Case 12-Month Return by Sector (Across Scenarios)
<img width="780" height="414" alt="WC12MRS" src="https://github.com/user-attachments/assets/7b21a6be-7441-4721-98bf-1431929b1e28" />
This chart highlights the maximum downside risk each sector faces across all scenarios. Financials show the largest potential losses, making them the most vulnerable during severe economic stress. Cyclical sectors such as consumer discretionary, industrials, and technology also experience significant drawdowns. Defensive sectors like utilities, healthcare, and consumer staples perform relatively better, though they are not immune to losses. Energy stands out as the most resilient sector, showing minimal downside even in worst-case conditions.

# Portfolio Cumulative Return Under Scenarios
<img width="587" height="455" alt="PCRUS" src="https://github.com/user-attachments/assets/775bd9b2-67a9-4719-9cc9-d0f7d6da8b65" />
This chart shows how an equal-weight portfolio evolves under different macroeconomic scenarios. The rate shock scenario results in the smallest decline, indicating that tightening alone is less damaging than broader economic stress. The recession scenario produces deeper losses as weaker demand impacts most sectors. Stagflation leads to the worst outcome, combining inflation pressure with slowing growth and causing losses to build over time. The chart clearly shows how risk increases as economic conditions worsen.

# Sector 12-Month Return Impact: Recession
<img width="780" height="414" alt="S12MRIR" src="https://github.com/user-attachments/assets/acf6205d-3d62-4513-83e9-8f24729244c6" />
This chart illustrates sector performance during a recession over a 12-month period. Financials experience the largest losses due to higher credit risk and reduced lending. Cyclical sectors like industrials, consumer discretionary, and technology also decline as demand weakens. Defensive sectors show smaller drawdowns, reflecting more stable cash flows. Energy performs positively, suggesting that commodity exposure can offset recessionary pressure.

# Sector 12-Month Return Impact: Stagflation
<img width="780" height="414" alt="S12MRISt" src="https://github.com/user-attachments/assets/12d190cf-e7dd-4047-aa22-0dbe0fc1cccd" />
Stagflation produces the most severe and broad-based losses across sectors. Financials, consumer discretionary, and industrials are hit hardest as rising costs and slowing growth strain profits. Technology and materials also perform poorly due to valuation pressure. Defensive sectors decline less but still face meaningful losses. Energy remains the most resilient sector, benefiting from inflation-linked dynamics.

# Sector 12-Month Return Impact: Rate Shock
<img width="789" height="414" alt="S12MRIRS" src="https://github.com/user-attachments/assets/466a1790-8069-49cb-8b2c-24772ffb84ea" />
This chart shows sector responses to a rapid increase in interest rates. Financials suffer notable losses, indicating that aggressive tightening can outweigh short-term benefits from higher rates. Growth-oriented sectors such as technology and consumer discretionary also decline due to valuation pressure. Defensive sectors experience smaller drawdowns and appear more insulated. Energy is the only sector with positive performance, reflecting its sensitivity to inflation rather than interest rates.



