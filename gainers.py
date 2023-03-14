# Description: This script will print the top gainers for the day, as well as other information about them.

import requests

# Set the API endpoint URL for the top stocks
top_stocks_endpoint = "https://mboum-finance.p.rapidapi.com/co/collections/day_gainers"

# Set the API key and host for the top stocks API
top_stocks_headers = {
    "X-RapidAPI-Key": "0rD6UyDj8jmshLwoCdZCWBgBf6pIp1UK2BBjsnb2kK9LFosz4o",
    "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
}

# Set the parameters for the top stocks API request
top_stocks_params = {"start": "0"}

# Make the API request for the top stocks
top_stocks_response = requests.get(
    top_stocks_endpoint, headers=top_stocks_headers, params=top_stocks_params
)

# Check the status code of the response for the top stocks
if top_stocks_response.status_code == 200:
    # Get the data from the response for the top stocks
    top_stocks_data = top_stocks_response.json()
    # Get the list of symbols for the top stocks
    symbols = [stock["symbol"] for stock in top_stocks_data["quotes"]]
    longName = [longName["longName"] for longName in top_stocks_data["quotes"]]
    fullExchangeName = [fullExchangeName["fullExchangeName"] for fullExchangeName in top_stocks_data["quotes"]]
    # Print the symbols for the top stocks
    #print(f"Top stocks: {symbols}")
    #print(f"Company Name: {longName}")
    # Create a list of dictionaries with the symbol and company name [{symbol: "", longName: ""},]
    list = []
    for i in range(len(symbols)):
        data = {'symbol': symbols[i], 'longName': longName[i], 'fullExchangeName': fullExchangeName[i]}
        list.append(data)
    print(list)


else:
    print(f"Error: {top_stocks_response.status_code}")

