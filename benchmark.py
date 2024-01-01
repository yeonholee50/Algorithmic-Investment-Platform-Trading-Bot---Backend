import ccxt
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch historical price data for a symbol from Yahoo Finance
def fetch_stock_data(symbol, start_date, end_date):
    import yfinance as yf
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data['Adj Close']

# Function to calculate daily returns
def calculate_daily_returns(df):
    return df.pct_change().dropna()

# Function to calculate cumulative returns
def calculate_cumulative_returns(returns):
    return (1 + returns).cumprod() - 1

# Function to visualize cumulative returns
def visualize_cumulative_returns(bot_returns, sp500_returns, start_date, end_date):
    plt.figure(figsize=(14, 8))

    plt.plot(bot_returns.index, bot_returns, label='Trading Bot', color='blue')
    plt.plot(sp500_returns.index, sp500_returns, label='S&P 500', color='orange')

    plt.title('Cumulative Returns Comparison')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' and 'YOUR_SECRET' with your actual API key and secret
    exchange = ccxt.binance({
        'apiKey': 'YOUR_API_KEY',
        'secret': 'YOUR_SECRET',
    })

    # Replace 'USD' with your desired trading pair
    trading_pair = 'USD'

    # Replace 'ETH/USD' and 'SPY' with your desired risk and benchmark symbols
    risk_asset_symbol = 'ETH/USD'
    benchmark_symbol = 'SPY'

    # Fetch historical data for the trading bot
    bot_data = exchange.fetch_ohlcv(trading_pair, '1d', limit=1000)
    bot_df = pd.DataFrame(bot_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    bot_df['timestamp'] = pd.to_datetime(bot_df['timestamp'], unit='ms')
    bot_df.set_index('timestamp', inplace=True)

    # Simulate portfolio and risk management for the trading bot
    initial_balance = 10000  # Replace with your initial balance
    risk_per_trade = 0.02    # Replace with your desired risk per trade

    # Existing simulation function
    bot_balance_history = simulate_portfolio(extended_signals, initial_balance, risk_per_trade)

    # Fetch historical data for the S&P 500
    sp500_data = fetch_stock_data(benchmark_symbol, start_date='2022-01-01', end_date='2023-01-01')

    # Calculate daily returns for the trading bot and S&P 500
    bot_returns = calculate_daily_returns(pd.Series(bot_balance_history, index=bot_df.index))
    sp500_returns = calculate_daily_returns(sp500_data)

    # Calculate cumulative returns
    bot_cumulative_returns = calculate_cumulative_returns(bot_returns)
    sp500_cumulative_returns = calculate_cumulative_returns(sp500_returns)

    # Visualize cumulative returns
    visualize_cumulative_returns(bot_cumulative_returns, sp500_cumulative_returns, bot_df.index[0], bot_df.index[-1])
