# Stock Portfolio Analyzer 📈

A Python-based stock portfolio analyzer that fetches real NSE (National Stock Exchange) data and performs comprehensive financial analysis.

## 🎯 Objective
Analyze 5 Indian blue-chip stocks to identify the best performing investment based on risk-adjusted returns, and benchmark portfolio performance against Nifty 50.

## 📊 Stocks Analyzed
| Stock | Company | Sector |
|-------|---------|--------|
| RELIANCE.NS | Reliance Industries | Energy & Retail |
| HDFCBANK.NS | HDFC Bank | Banking |
| TCS.NS | Tata Consultancy Services | IT |
| INFY.NS | Infosys | IT |
| WIPRO.NS | Wipro | IT |

## 🔧 Libraries Used
- `yfinance` — Real-time NSE stock data
- `pandas` — Data processing
- `matplotlib` — Visualizations
- `seaborn` — Advanced charts

## 📈 Analysis Performed
- **Daily Returns** — Percentage change in stock price each day
- **Annual Volatility** — Risk measurement using standard deviation
- **Sharpe Ratio** — Risk-adjusted return (Risk-free rate: 6.5% India 10Y Bond)
- **Nifty 50 Benchmark** — Portfolio performance vs index

## 🏆 Key Findings (2023-2024)
| Stock | Sharpe Ratio | Annual Volatility | Verdict |
|-------|-------------|-------------------|---------|
| WIPRO | 0.79 | 24.17% | Best ✅ |
| TCS | 0.55 | 19.70% | Good ✅ |
| INFY | 0.46 | 23.09% | Average |
| HDFCBANK | 0.06 | 19.82% | Weak |
| RELIANCE | -0.15 | 20.36% | Underperformed ❌ |

- WIPRO outperformed Nifty 50 with 1.6x growth
- RELIANCE negative Sharpe — risk taken without adequate return

## 🚀 How to Run
```bash
pip install yfinance pandas matplotlib seaborn
python portfolio_analyzer.py
```

## 📁 Output
- `portfolio_analysis.png` — 4-chart dashboard
- `benchmark_comparison.png` — Portfolio vs Nifty 50
