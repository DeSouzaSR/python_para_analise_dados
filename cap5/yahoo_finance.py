
#%%
import yfinance as yf

#%%
# Lista de ações
tickers = ['AAPL', 'IBM', 'MSFT', 'GOOG']

#%%
# Baixar dados para todas as ações
all_data = {ticker: yf.download(ticker) for ticker in tickers}

#%%
# Exibir dados de uma ação
print(all_data['AAPL'].head())
