# Description: Make an api call that returns options on a particular stock


import requests

def options(symbol):
    url = "https://mboum-finance.p.rapidapi.com/op/option"

    querystring = {"expiration":"1705622400","symbol":symbol}

    headers = {
	    "X-RapidAPI-Key": "0rD6UyDj8jmshLwoCdZCWBgBf6pIp1UK2BBjsnb2kK9LFosz4o",
	    "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response_text = (response.text)