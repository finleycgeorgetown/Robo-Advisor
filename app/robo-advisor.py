# app/robo_advisor.py

import csv
import os
import json

from dotenv import load_dotenv
import requests

from datetime import datetime
now = datetime.now()
datelabel = now.strftime("%d/%m/%Y %H:%M:%S")


load_dotenv()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


#
#INFO INPUTS
#

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

stock = str(input("Which stock do you wish to check? "))
stock_upper = stock.upper()
if len(stock_upper) >=1 or 5 >= len(stock_upper):
    symbol = stock_upper
elif len(stock_upper) > 5:
    print("please enter a valid stock")
    quit()
else:
    quit()


request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
response = requests.get(request_url)

#print(type(response)) #> <class 'requests.models.Response'>
#print(response.status_code) #> 200
#print(response.text) 

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
#breakpoint()

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) # TODO: sort to ensure latest day is 1st
latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]

#max of all high prices
high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)
#breakpoint()

#
#INFO OUTPUTS
#


csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file: 
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"],
    })


stock_decision = ""
decision_reason = ""
if float(latest_close) < (1.2 * float(recent_low)):
    stock_decision = "Buy!"
    decision_reason = "The latest closing price is within 20 percent of the recent low"
else:
    stock_decision = "Don't Buy."
    decision_reason = "The latest closing price is not within 20 percent of the recent low"

print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {datelabel}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print(f"RECOMMENDATION: {stock_decision}")
print(f"RECOMMENDATION REASON: {decision_reason}")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

