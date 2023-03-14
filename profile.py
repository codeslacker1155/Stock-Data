# Description: This is is a ticker company profile query that will be used to gather info about a particular stock ticker or company.
import requests

# import gainers.py
from gainers import symbols, longName, fullExchangeName, list

# Create a function for the company that takes a symbol as a string argument
def profile(symbol):
    # Set the API endpoint URL for the asset profile
    asset_profile_endpoint = (
        "https://mboum-finance.p.rapidapi.com/qu/quote/asset-profile"
    )

    # Set the API key and host for the asset profile API
    asset_profile_headers = {
        "X-RapidAPI-Key": "0rD6UyDj8jmshLwoCdZCWBgBf6pIp1UK2BBjsnb2kK9LFosz4o",
        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com",
    }

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
        # Print the data for the asset profile
        #print(f"Asset Profile: {asset_profile_data}")
        address = asset_profile_data['assetProfile']["address1"]
        city = asset_profile_data['assetProfile']["city"]
        state = asset_profile_data['assetProfile']["state"]
        zip = asset_profile_data['assetProfile']["zip"]
        country = asset_profile_data['assetProfile']["country"]
        phone = asset_profile_data['assetProfile']["phone"]
        website = asset_profile_data['assetProfile']["website"]
        industry = asset_profile_data['assetProfile']["industry"]
        sector = asset_profile_data['assetProfile']["sector"]
        fullTimeEmployees = asset_profile_data['assetProfile']["fullTimeEmployees"]
        longBusinessSummary = asset_profile_data['assetProfile']["longBusinessSummary"]
        auditRisk = asset_profile_data['assetProfile']["auditRisk"]
        boardRisk = asset_profile_data['assetProfile']["boardRisk"]
        compensationRisk = asset_profile_data['assetProfile']["compensationRisk"]
        shareHolderRightsRisk = asset_profile_data['assetProfile']["shareHolderRightsRisk"]
        overallRisk = asset_profile_data['assetProfile']["overallRisk"]

        # get list of companyOfficers
        companyOfficers = asset_profile_data['assetProfile']["companyOfficers"]
        officers = []
        # Note: Some of the companyOfficers variables being referenced dont exist
        for officer in companyOfficers:
            name = officer.get("name", "N/A")
            title = officer.get("title", "N/A")
            age = officer.get("age", "N/A")
            yearBorn = officer.get("yearBorn", "N/A")
            totalPay = officer.get("totalPay", {}).get('raw', "N/A")
            totalPay_long = officer.get("totalPay", {}).get('longFmt', "N/A")
            totalPay_fmt = officer.get("totalPay", {}).get('fmt', "N/A")
            exercisedValue = officer.get("exercisedValue", {}).get('raw', "N/A")
            exercisedValue_long = officer.get("exercisedValue", {}).get('longFmt', "N/A")
            exercisedValue_fmt = officer.get("exercisedValue", {}).get('fmt', "N/A")
            # create a dictionary of companyOfficers {name: "", title: "", age: "", yearBorn: "", totalPay: "", exercisedValue: ""}
            data = {'name': name, 'title': title, 'age': age, 'yearBorn': yearBorn, 'totalPay': totalPay, 'totalPay_long': totalPay_long, 'totalPay_fmt': totalPay_fmt, 'exercisedValue': exercisedValue, 'exercisedValue_long': exercisedValue_long, 'exercisedValue_fmt': exercisedValue_fmt}
            officers.append(data)
        print(officers)

    else:
        print(f"Error: {asset_profile_response.status_code}")
        
# Input: {ticker}

# Output: company {address, city, state, zip, country, phone, website, industry, sector, fullTimeEmployees, longBusinessSummary, auditRisk, boardRisk, compensationRisk, shareHolderRightsRisk, overallRisk, officers}