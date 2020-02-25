# Robo-Advisor
Robo Advisor Project

## Prerequisites

-Anaconda 3.7
-Python 3.7
-Pip

# Setup
Before using this application, [obtain an AlphaVantage API Key](https://www.alphavantage.co/support/#api-key)

After obtaining an API Key, create a new file in this repository called ".env", and update the contents of the ".env" file to specify your real API key.


## Repo Setup
Download [this repository](https://github.com/finleycgeorgetown/Robo-Advisor) onto your computer via GitHub, and then navigate to the dircetory that it is saved under, followed by:

```
cd Robo-Advisor
```
When prompted, make sure to attatch a README.md and a Python-flavored .gitignore file, along with a licence to your repository. 

## Enviornment Setup
Use Anaconda to create and activate a new virtual enviornment.

```
conda create -n stocks-env python=3.7
conda activate stocks-env
```
## Text Editor Setup
Use your text editor to verify a  file called "requirements.txt", and verify that  the following contents are inside:

```
requests
python-dotenv
```

# App Function
## Information Inputs
The system will prompt the user to input one stocksymbol (e.g. "MSFT", "AAPL", etc.)
## Validation 
The app will first check to make sure the input is within a reasonable length for validation in stock price checking, otherwise the user will recieve a prompt to enter a valid string and will exit the program. If preliminary validations are satisfied, the system should proceed to issue a GET request to the AlphaVantage API to retrieve corresponding stock market data.

When the system makes an HTTP request for that stock symbol's trading data, if the stock symbol is not found or if there is an error message returned by the API server, the system should display a friendly error message.
## Output
After receiving a successful API response, the system should write historical stock prices to one or more CSV files located in the repository's "data" directory. The CSV file contents should resemble the following example:
```
timestamp, open, high, low, close, volume
2018-06-04, 101.2600, 101.8600, 100.8510, 101.6700, 27172988
2018-06-01, 99.2798, 100.8600, 99.1700, 100.7900, 28655624
2018-05-31, 99.2900, 99.9900, 98.6100, 98.8400, 34140891
2018-05-30, 98.3100, 99.2500, 97.9100, 98.9500, 22158528
```

After writing historical data to a CSV file, the system should perform calculations (see "Calculation Requirements" section below) to produce/print the following outputs:

-The selected stock symbol (e.g. "Stock: MSFT")

-The date and time when the program was executed.

-The date when the data was last refreshed, usually the same as the latest available day of daily trading data (e.g. "Latest Data from: June 4th, 2018")

For the stock symbol: 

-The latest closing price 

-The recent high price

-The recent low price

-A recommendation as to whether or not the client should buy the stock

-A recommendation explanation


## [License](/LICENSE)

