import yfinance as yf
import streamlit as st




st.write("""
# Stock Price Web App
         

Shown are the stock closing price and volume!

""")


#Ticker symbols-->
#Google-GOOGL
#Microsoft-MSFT
#Tesla-TSLA
#Amazon-AMZN


#define the ticker symbol
tickerSymbol = 'AMZN'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2023-8-31')


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)