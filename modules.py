# Perform an api call from a list of methods to get data about a particular stock ticker

import requests

url = "https://mboum-finance.p.rapidapi.com/mo/module/"


# you can pass up to 5 modules in the querystring from the list below
# asset-profile, income-statement, balance-sheet, cashflow-statement, default-key-statistics, calendar-events, sec-filings, upgrade-downgrade-history, institution-ownership, fund-ownership, insider-transactions, insider-holders, earnings-history
querystring = {"symbol":"AAPL","module":"asset-profile,financial-data,insider-holders,institution-ownership,default-key-statistics"}

headers = {
	"X-RapidAPI-Key": "0rD6UyDj8jmshLwoCdZCWBgBf6pIp1UK2BBjsnb2kK9LFosz4o",
	"X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

if response.status_code == 200:
        # Get the data from the response for the asset profile
        response_data = response.json()
        print(response_data)