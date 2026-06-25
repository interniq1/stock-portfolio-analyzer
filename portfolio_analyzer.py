# Step 1: Libraries Import karo
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Step 2: Stocks define karo (NSE Indian Stocks)
stocks = ['RELIANCE.NS', 'HDFCBANK.NS', 'TCS.NS', 'INFY.NS', 'WIPRO.NS']

# Step 3: Date range set karo
start_date = '2023-01-01'
end_date = '2024-12-31'

# Step 4: Data download karo
print("Downloading stock data...")
data = yf.download(stocks, start=start_date, end=end_date)['Close']

# Step 5: Check karo data aaya ya nahi
print("\nData shape:", data.shape)
print("\nFirst 5 rows:")
print(data.head())

# Step 6: Daily Returns calculate karo
returns = data.pct_change().dropna()

print("\nDaily Returns (first 5 rows):")
print(returns.head())

print("\nAverage Daily Return (%):")
print((returns.mean() * 100).round(4))

# Step 7: Risk Metrics calculate karo
risk_free_rate = 0.065 / 252  # India 10-year bond rate (annualized to daily)

# Volatility (Annual)
volatility = returns.std() * (252 ** 0.5)

# Sharpe Ratio
sharpe_ratio = (returns.mean() - risk_free_rate) / returns.std() * (252 ** 0.5)

# Summary Table
summary = pd.DataFrame({
    'Avg Daily Return (%)': (returns.mean() * 100).round(4),
    'Annual Volatility (%)': (volatility * 100).round(2),
    'Sharpe Ratio': sharpe_ratio.round(2)
})

print("\n========= PORTFOLIO RISK ANALYSIS =========")
print(summary)
print("===========================================")

# Step 8: Charts banana
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Stock Portfolio Analysis (2023-2024)', fontsize=16, fontweight='bold')

# Chart 1: Stock Price Trend
data.plot(ax=axes[0, 0], title='Stock Price Trend')
axes[0, 0].set_ylabel('Price (INR)')
axes[0, 0].set_xlabel('')

# Chart 2: Daily Returns
returns.plot(ax=axes[0, 1], title='Daily Returns', alpha=0.7)
axes[0, 1].set_ylabel('Return')
axes[0, 1].set_xlabel('')

# Chart 3: Sharpe Ratio Bar Chart
sharpe_ratio.plot(kind='bar', ax=axes[1, 0], title='Sharpe Ratio Comparison', color='steelblue')
axes[1, 0].set_ylabel('Sharpe Ratio')
axes[1, 0].axhline(y=0.5, color='red', linestyle='--', label='Good (0.5)')
axes[1, 0].legend()

# Chart 4: Volatility Bar Chart
(volatility * 100).plot(kind='bar', ax=axes[1, 1], title='Annual Volatility (%)', color='coral')
axes[1, 1].set_ylabel('Volatility (%)')

plt.tight_layout()
plt.savefig('portfolio_analysis.png', dpi=150)
plt.show()
print("\nChart saved as portfolio_analysis.png")

# Step 9: Nifty 50 Benchmark comparison
nifty = yf.download('^NSEI', start=start_date, end=end_date)['Close']
nifty_returns = nifty.pct_change().dropna()

# Cumulative Returns
cumulative_portfolio = (1 + returns).cumprod()
cumulative_nifty = (1 + nifty_returns).cumprod()

# Plot
plt.figure(figsize=(12, 6))
for stock in stocks:
    plt.plot(cumulative_portfolio[stock], label=stock, alpha=0.7)
plt.plot(cumulative_nifty, label='NIFTY 50', color='black', linewidth=2.5, linestyle='--')
plt.title('Portfolio vs Nifty 50 (Cumulative Returns 2023-2024)', fontsize=14)
plt.ylabel('Growth of ₹1 Invested')
plt.xlabel('Date')
plt.legend()
plt.tight_layout()
plt.savefig('benchmark_comparison.png', dpi=150)
plt.show()
print("\nBenchmark chart saved!")
