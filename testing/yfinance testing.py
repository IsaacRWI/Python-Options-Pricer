import yfinance as yf
from datetime import datetime

def dateToString(date):
    date = date.strftime("%Y-%m-%d")
    return date

# df = yf.download("GOOG", start=dateToString(datetime.now()), multi_level_index=False)

# print(dateToString(datetime.now()))
# print(df.info)

# print(df[["Close"]])

# close = df["Close"].tolist()[0]
# print(close)

df = yf.download("GOOG", start=datetime.now().strftime("%Y-%m-%d"), multi_level_index=False, auto_adjust=True)
# print(df.info)
close = df["Close"].tolist()[0]
print(close)