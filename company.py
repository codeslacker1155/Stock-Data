# Description: This is is a company class that will be used to gather info about a particular stock ticker or company.
import requests

# import gainers.py
from gainers import symbols, longName, fullExchangeName, list

# Create a class for the company that takes a symbol as a string argument
class Company(symbol):
    # Set the API endpoint URL for the asset profile
    asset_profile_endpoint = (
        "https://mboum-finance.p.rapidapi.com/qu/quote/asset-profile"
    )

    # Set the API key and host for the asset profile API
    asset_profile_headers = {
        "X-RapidAPI-Key": "0rD6UyDj8jmshLwoCdZCWBgBf6pIp1UK2BBjsnb2kK9LFosz4o",
        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com",
    }
    for symbol in symbols:

    # Set the parameters for the asset profile API request
    asset_profile_params = {"symbol": symbol}

    # Make the API request for the asset profile
    asset_profile_response = requests.get(
        asset_profile_endpoint,
        headers=asset_profile_headers,
        params=asset_profile_params,
    )

    # Check the status code of the response for the asset profile
    if asset_profile_response.status_code == 200:
        # Get the data from the response for the asset profile
        asset_profile_data = asset_profile_response.json()
