import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate the maximum drawdown of the portfolio
def calculate_max_drawdown(returns):
    cumulative_returns = (1 + returns).cumprod() - 1
    peak = cumulative_returns.expanding(min_periods=1).max()
    drawdown = (cumulative_returns - peak) / (peak + 1e-8)  # Avoid division by zero
    max_drawdown = drawdown.min()
    return max_drawdown

# Function to visualize drawdowns over time
def visualize_drawdowns(returns, start_date, end_date):
    plt.figure(figsize=(14, 8))

    cumulative_returns = (1 + returns).cumprod() - 1
    peak = cumulative_returns.expanding(min_periods=1).max()
    drawdown = (cumulative_returns - peak) / (peak + 1e-8)  # Avoid division by zero

    plt.plot(returns.index, drawdown, label='Drawdown', color='red')

    plt.title('Portfolio Drawdowns')
    plt.xlabel('Date')
    plt.ylabel('Drawdown')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to calculate the Sharpe ratio
def calculate_sharpe_ratio(returns, risk_free_rate=0):
    annualized_return = returns.mean() * 252  # Assuming 252 trading days in a year
    annualized_volatility = returns.std() * (252 ** 0.5)
    sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility
    return sharpe_ratio

# Function to calculate rolling Sharpe ratio
def calculate_rolling_sharpe_ratio(returns, window=20, risk_free_rate=0):
    rolling_sharpe_ratio = returns.rolling(window=window).apply(calculate_sharpe_ratio, args=(risk_free_rate,))
    return rolling_sharpe_ratio

# Function to visualize performance metrics over time
def visualize_performance_metrics(returns, drawdowns, sharpe_ratios, rolling_sharpe_ratios, start_date, end_date):
    plt.figure(figsize=(14, 12))

    cumulative_returns = (1 + returns).cumprod() - 1

    plt.subplot(4, 1, 1)
    plt.plot(returns.index, cumulative_returns, label='Cumulative Returns', color='green')
    plt.title('Cumulative Returns')

    plt.subplot(4, 1, 2)
    plt.plot(drawdowns.index, drawdowns, label='Drawdown', color='red')
    plt.title('Drawdowns')

    plt.subplot(4, 1, 3)
    plt.plot(sharpe_ratios.index, sharpe_ratios, label='Sharpe Ratio', color='blue')
    plt.title('Sharpe Ratio')

    plt.subplot(4, 1, 4)
    plt.plot(rolling_sharpe_ratios.index, rolling_sharpe_ratios, label='Rolling Sharpe Ratio', color='purple')
    plt.title('Rolling Sharpe Ratio')

    plt.xlabel('Date')
    plt.tight_layout()
    plt.show()

# Function to calculate and visualize rolling correlation with a benchmark
def visualize_rolling_correlation(returns, benchmark_returns, window=20, start_date=None, end_date=None):
    rolling_corr = returns.rolling(window=window).corr(benchmark_returns)
    
    plt.figure(figsize=(14, 6))
    plt.plot(rolling_corr.index, rolling_corr, label='Rolling Correlation', color='orange')
    
    plt.title('Rolling Correlation with Benchmark')
    plt.xlabel('Date')
    plt.ylabel('Correlation')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    pass 
