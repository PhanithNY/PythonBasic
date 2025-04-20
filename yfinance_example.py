import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import  datetime

from fontTools.misc.plistlib import end_date
from pandas.core.arrays import period_array

plt.style.use("default")

msft = yf.Ticker("msft")

# stock_info = msft.info
# number_of_share = stock_info["sharesOutstanding"]
# print(f"Number of share: ", number_of_share)
#
# dividends = msft.dividends
# print(f"Dividends: ", dividends)
#
# holders = msft.institutional_holders
# print(f"Holders: ", holders, sep="\n")
#
# # Sum dividend by year-end
# data = dividends.resample("YE").sum()
# print("Data after sum: \n", data)
#
# data = data.reset_index()
# print("Data after reset_index: \n", data)
#
# # Create new colum Year, insert year from "Date" into that column
# data["Year"] = data["Date"].dt.year
# print("Data after new column: \n", data)
#
# plt.figure()
# plt.bar(data["Year"], data["Dividends"])
# plt.xlabel("Year")
# plt.ylabel("Dividends ($)")
# plt.title("Hello")
# # plt.xlim(2004, 2024)
# plt.show()

# data_frames = msft.history(period="max")
data_frames = msft.history(start="2010-01-10",end="2025-01-10")
plt.figure()
plt.plot(data_frames["Close"])
plt.show()