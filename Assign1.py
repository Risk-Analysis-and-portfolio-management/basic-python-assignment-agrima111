#!/usr/bin/env python
# coding: utf-8

# In[48]:


pip install yfinance


# In[49]:


#Question1


# In[50]:


from datetime import datetime 
import yfinance as yf 
import matplotlib.pyplot as plt 
  
start_date = datetime(2023, 12, 12) 
end_date = datetime(2024, 12, 12) 
  
data = yf.download('AAPL', start = start_date, end = end_date) 
  
plt.figure(figsize = (20,10)) 
plt.title('Closing Prices from {} to {}'.format(start_date, end_date)) 
plt.plot(data['Close']) 
plt.show()


# In[51]:


#The above graph shows that the closing price of apple stock has a sell off trend from jan to May
#Then the graph shows a rally trend from May till July
#then the graph goes with range trend with not much price variation from August till November


# In[52]:


#question2


# In[53]:


import pandas as pd
total_investment = 10000
stocks = ['AAPL', 'MSFT', 'GOOGL']  
investment_per_stock = 10000 /3  
start_date = '2024-06-01'
end_date = '2024-12-01'

data = yf.download(stocks, start=start_date, end=end_date)['Close']
daily_returns = data.pct_change()
weights = [1/len(stocks)] * len(stocks)
portfolio_daily_returns = daily_returns.dot(weights)
portfolio_cumulative_returns = (1 + portfolio_daily_returns).cumprod()
portfolio_values = portfolio_cumulative_returns * total_investment
final_portfolio_value = portfolio_values.iloc[-1]

initial_shares = {stock: investment_per_stock / data[stock].iloc[0] for stock in stocks}

plt.figure(figsize=(20,10))
portfolio_values.plot(title='Portfolio Value Over Time')
plt.xlabel('Date')
plt.ylabel('Portfolio Value')
print(f"Final Portfolio Value: {final_portfolio_value:}")


# In[54]:


#Question3


# In[55]:


def analyze_portfolio(tickers, weights, start_date, end_date):
    initial_investment=100000
    data = yf.download(tickers, start=start_date, end=end_date)['Close']
    daily_returns = data.pct_change()
    portfolio_daily_returns = daily_returns.dot(weights)
    portfolio_cumulative_returns = (1 + portfolio_daily_returns).cumprod()
    portfolio_values = portfolio_cumulative_returns * initial_investment
    final_portfolio_value = portfolio_values.iloc[-1]
    plt.figure(figsize=(20, 10))
    portfolio_values.plot(title='Portfolio Value Over Time')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value')
    plt.show()
    return final_portfolio_value

tickers = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'NVDA']
weights = [0.3, 0.2, 0.2, 0.2, 0.1]
start_date = '2023-01-01'
end_date = '2023-12-31'
final_value = analyze_portfolio(tickers, weights, start_date, end_date)
print(f"The final value of the portfolio is: {final_value:}")


# In[ ]:





# In[ ]:




