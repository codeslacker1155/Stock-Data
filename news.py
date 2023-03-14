# Description: Get the news for a particular stock ticker or company.

import requests

def news(symbol):
    url = "https://mboum-finance.p.rapidapi.com/ne/news/"

    querystring = {"symbol":symbol}

    headers = {
	    "X-RapidAPI-Key": "0rD6UyDj8jmshLwoCdZCWBgBf6pIp1UK2BBjsnb2kK9LFosz4o",
	    "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response_text = (response.text)
