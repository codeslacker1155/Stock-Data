# Description: Perform an api call from a list of methods to get data about a particular stock ticker

import requests

def modules(symbol):
        url = "https://mboum-finance.p.rapidapi.com/mo/module/"

        # you can pass up to 5 modules in the querystring from the list below
        # asset-profile, income-statement, balance-sheet, cashflow-statement, default-key-statistics
        # calendar-events, sec-filings, upgrade-downgrade-history, institution-ownership, fund-ownership
        # insider-transactions, insider-holders, earnings-history
        querystring = {"symbol":symbol,"module":"asset-profile,financial-data,insider-holders,institution-ownership,default-key-statistics"}

        headers = {
	        "X-RapidAPI-Key": "0rD6UyDj8jmshLwoCdZCWBgBf6pIp1UK2BBjsnb2kK9LFosz4o",
	        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        if response.status_code == 200:
                # Get the data from the response for the asset profile
                response_data = response.json()
                print(response_data)
                address = response_data['assetProfile']["address1"]
                city = response_data['assetProfile']["city"]
                state = response_data['assetProfile']["state"]
                zip = response_data['assetProfile']["zip"]
                country = response_data['assetProfile']["country"]
                phone = response_data['assetProfile']["phone"]
                website = response_data['assetProfile']["website"]
                industry = response_data['assetProfile']["industry"]
                sector = response_data['assetProfile']["sector"]
                fullTimeEmployees = response_data['assetProfile']["fullTimeEmployees"]
                longBusinessSummary = response_data['assetProfile']["longBusinessSummary"]
                auditRisk = response_data['assetProfile']["auditRisk"]
                boardRisk = response_data['assetProfile']["boardRisk"]
                compensationRisk = response_data['assetProfile']["compensationRisk"]
                shareHolderRightsRisk = response_data['assetProfile']["shareHolderRightsRisk"]
                overallRisk = response_data['assetProfile']["overallRisk"]
                
                # get list of companyOfficers
                companyOfficers = response_data['assetProfile']["companyOfficers"]
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
                
                # get list of institutionalOwnership
                institutionalOwnership = response_data['institutionOwnership']['ownershipList']
                institutions = []
                for institution in institutionalOwnership:
                        reportDate = institution.get("reportDate", {}).get('fmt', "N/A")
                        institutionName = institution.get("organization", "N/A")
                        pctHeld = institution.get("pctHeld", {}).get('raw', "N/A")
                        pctHeld_fmt = institution.get("pctHeld", {}).get('fmt', "N/A")
                        shares = institution.get("position", {}).get('raw', "N/A")
                        shares_long = institution.get("position", {}).get('longFmt', "N/A")
                        shares_fmt = institution.get("position", {}).get('fmt', "N/A")
                        value = institution.get("value", {}).get('raw', "N/A")
                        value_long = institution.get("value", {}).get('longFmt', "N/A")
                        value_fmt = institution.get("value", {}).get('fmt', "N/A")
                        # create a dictionary of institutionalOwnership {institutionName: "", position: "", shares: ""}
                        institution_data = {"reportDate": reportDate, "organization": institutionName, "pctHeld": pctHeld_fmt, "sharesHeld": shares_fmt, "shareValue": value_fmt}
                        institutions.append(institution_data)
                
                # get a list of insiderHolders
                insiderHolders = response_data['insiderHolders']['holders']
                insiders = []
                for insider in insiderHolders:
                        name = insider.get("name", "N/A")
                        relation = insider.get("relation", "N/A")
                        transactionDesc = insider.get("transactionDescription", "N/A")
                        latestTransDate = insider.get("latestTransDate", {}).get("raw", "N/A")
                        latestTransDate_fmt = insider.get("latestTransDate", {}).get("fmt", "N/A")
                        position = insider.get("positionDirect", {}).get("raw", "N/A")
                        position_fmt = insider.get("positionDirect", {}).get("fmt", "N/A")
                        position_long = insider.get("positionDirect", {}).get("longFmt", "N/A")
                        positionDate = insider.get("positionDirectDate", {}).get("raw", "N/A")
                        positionDate_fmt = insider.get("positionDirectDate", {}).get("fmt", "N/A")
                        # create a dictionary of insiders {"name": name, "relation": relation, "transactionDesc": transactionDesc, "latestTransDate": latestTransDate_fmt, "sharesOwned": position_fmt, "sharesOwnedDate": positionDate_fmt}
                        insiders_data = {"name": name, "relation": relation, "transactionDesc": transactionDesc, "latestTransDate": latestTransDate_fmt, "sharesOwned": position_fmt, "sharesOwnedDate": positionDate_fmt}
                        insiders.append(insiders_data)
                
                # get a list of defaultKeyStatistics
                defaultKeyStatistics = response_data['defaultKeyStatistics']
                enterpriseValue = defaultKeyStatistics.get("enterpriseValue", {}).get("raw", "N/A")
                enterpriseValue_fmt = defaultKeyStatistics.get("enterpriseValue", {}).get("fmt", "N/A")
                enterpriseValue_long = defaultKeyStatistics.get("enterpriseValue", {}).get("longFmt", "N/A")
                forwardPE = defaultKeyStatistics.get("fowardPE", {}).get("raw", "N/A")
                forwardPE_fmt = defaultKeyStatistics.get("fowardPE", {}).get("fmt", "N/A")
                profitMargins = defaultKeyStatistics.get("profitMargins", {}).get("raw", "N/A")
                profitMargins_fmt = defaultKeyStatistics.get("profitMargins", {}).get("fmt", "N/A")
                


# Call modules function with a stock ticker
modules("AAPL")