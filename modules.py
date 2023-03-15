# Description: Perform an api call from a list of methods to get data about a particular stock ticker 

# Default Modules: asset-profile, financial-data, insider-holders, institution-ownership, default-key-statistics

# Available Modules: asset-profile, income-statement, balance-sheet, cashflow-statement, default-key-statistics, calendar-events, sec-filings, upgrade-downgrade-history, institution-ownership, fund-ownership, insider-transactions, insider-holders, earnings-history

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
                floatShares = defaultKeyStatistics.get("floatShares", {}).get("raw", "N/A")
                floatShares_fmt = defaultKeyStatistics.get("floatShares", {}).get("fmt", "N/A")
                floatShares_long = defaultKeyStatistics.get("floatShares", {}).get("long", "N/A")
                sharesOutstanding = defaultKeyStatistics.get("sharesOutstanding", {}).get("raw", "N/A")
                sharesOutstanding_fmt = defaultKeyStatistics.get("sharesOutstanding", {}).get("fmt", "N/A")
                sharesOutstanding_long = defaultKeyStatistics.get("sharesOutstanding", {}).get("long", "N/A")
                sharesShort = defaultKeyStatistics.get("sharesShort", {}).get("raw", "N/A")
                sharesShort_fmt = defaultKeyStatistics.get("sharesShort", {}).get("fmt", "N/A")
                sharesShort_long = defaultKeyStatistics.get("sharesShort", {}).get("long", "N/A")
                sharesShortPriorMonth = defaultKeyStatistics.get("sharesShort", {}).get("raw", "N/A")
                sharesShortPriorMonth_fmt = defaultKeyStatistics.get("sharesShort", {}).get("fmt", "N/A")
                sharesShortPriorMonth_long = defaultKeyStatistics.get("sharesShort", {}).get("long", "N/A")
                sharesShortPriorMonthDate = defaultKeyStatistics.get("sharesShortPriorMonthDate", {}).get("raw", "N/A")
                sharesShortPriorMonthDate_fmt = defaultKeyStatistics.get("sharesShortPriorMonthDate", {}).get("fmt", "N/A")
                dateShortInterest = defaultKeyStatistics.get("dateShortInterest", {}).get("raw", "N/A")
                dateShortInterest_fmt = defaultKeyStatistics.get("dateShortInterest", {}).get("fmt", "N/A")
                sharesPercentSharesOut = defaultKeyStatistics.get("sharesPercentSharesOut", {}).get("raw", "N/A")
                sharesPercentSharesOut_fmt = defaultKeyStatistics.get("sharesPercentSharesOut", {}).get("fmt", "N/A")
                heldPercentInsiders = defaultKeyStatistics.get("heldPercentInsiders", {}).get("raw", "N/A")
                heldPercentInsiders_fmt = defaultKeyStatistics.get("heldPercentInsiders", {}).get("fmt", "N/A")
                heldPercentInstitutions = defaultKeyStatistics.get("heldPercentInstitutions", {}).get("raw", "N/A")
                heldPercentInstitutions_fmt = defaultKeyStatistics.get("heldPercentInstitutions", {}).get("fmt", "N/A")
                shortRatio = defaultKeyStatistics.get("shortRatio", {}).get("raw", "N/A")
                shortRatio_fmt = defaultKeyStatistics.get("shortRatio", {}).get("fmt", "N/A")
                shortPercentOfFloat = defaultKeyStatistics.get("shortPercentOfFloat", {}).get("raw", "N/A")
                shortPercentOfFloat_fmt = defaultKeyStatistics.get("shortPercentOfFloat", {}).get("fmt", "N/A")
                beta = defaultKeyStatistics.get("beta", {}).get("raw", "N/A")
                beta_fmt = defaultKeyStatistics.get("beta", {}).get("fmt", "N/A")
                impliedSharesOutstanding = defaultKeyStatistics.get("impliedSharesOutstanding", {}).get("raw", "N/A")
                impliedSharesOutstanding_fmt = defaultKeyStatistics.get("impliedSharesOutstanding", {}).get("fmt", "N/A")
                impliedSharesOutstanding_long = defaultKeyStatistics.get("impliedSharesOutstanding", {}).get("long", "N/A")
                morningStarOverallRating = defaultKeyStatistics.get("morningStarOverallRating", {}).get("raw", "N/A")
                morningStarOverallRating_fmt = defaultKeyStatistics.get("morningStarOverallRating", {}).get("fmt", "N/A")
                morningStarRiskRating = defaultKeyStatistics.get("morningStarRiskRating", {}).get("raw", "N/A")
                morningStarRiskRating_fmt = defaultKeyStatistics.get("morningStarRiskRating", {}).get("fmt", "N/A")
                category = defaultKeyStatistics.get("category", "N/A")
                bookValue = defaultKeyStatistics.get("bookValue", {}).get("raw", "N/A")
                bookValue_fmt = defaultKeyStatistics.get("bookValue", {}).get("fmt", "N/A")
                priceToBook = defaultKeyStatistics.get("priceToBook", {}).get("raw", "N/A")
                priceToBook_fmt = defaultKeyStatistics.get("priceToBook", {}).get("fmt", "N/A")
                annualReportExpenseRatio = defaultKeyStatistics.get("annualReportExpenseRatio", {}).get("raw", "N/A")
                annualReportExpenseRatio_fmt = defaultKeyStatistics.get("annualReportExpenseRatio", {}).get("fmt", "N/A")
                ytdReturn = defaultKeyStatistics.get("ytdReturn", {}).get("raw", "N/A")
                ytdReturn_fmt = defaultKeyStatistics.get("ytdReturn", {}).get("fmt", "N/A")
                beta3Year = defaultKeyStatistics.get("beta3Year", {}).get("raw", "N/A")
                beta3Year_fmt = defaultKeyStatistics.get("beta3Year", {}).get("fmt", "N/A")
                totalAssets = defaultKeyStatistics.get("totalAssets", {}).get("raw", "N/A")
                totalAssets_fmt = defaultKeyStatistics.get("totalAssets", {}).get("fmt", "N/A")
                yieldOverall = defaultKeyStatistics.get("yield", {}).get("fmt", "N/A")
                fundFamily = defaultKeyStatistics.get("fundFamily", "N/A")
                fundInceptionDate = defaultKeyStatistics.get("fundInceptionDate", {}).get("fmt", "N/A")
                legalType = defaultKeyStatistics.get("legalType", "N/A")
                threeYearAverageReturn = defaultKeyStatistics.get("threeYearAverageReturn", {}).get("raw", "N/A")
                threeYearAverageReturn_fmt = defaultKeyStatistics.get("threeYearAverageReturn", {}).get("fmt", "N/A")
                fiveYearAverageReturn = defaultKeyStatistics.get("fiveYearAverageReturn", {}).get("raw", "N/A")
                fiveYearAverageReturn_fmt = defaultKeyStatistics.get("fiveYearAverageReturn", {}).get("fmt", "N/A")
                priceToSalesTrailing12Months = defaultKeyStatistics.get("priceToSalesTrailing12Months", {}).get("raw", "N/A")
                lastFiscalYearEnd = defaultKeyStatistics.get("lastFiscalYearEnd", {}).get("raw", "N/A")
                lastFiscalYearEnd_fmt = defaultKeyStatistics.get("lastFiscalYearEnd", {}).get("fmt", "N/A")
                nextFiscalYearEnd = defaultKeyStatistics.get("nextFiscalYearEnd", {}).get("raw", "N/A")
                nextFiscalYearEnd_fmt = defaultKeyStatistics.get("nextFiscalYearEnd", {}).get("fmt", "N/A")
                mostRecentQuarter = defaultKeyStatistics.get("mostRecentQuarter", {}).get("raw", "N/A")
                mostRecentQuarter_fmt = defaultKeyStatistics.get("mostRecentQuarter", {}).get("fmt", "N/A")
                earningsQuarterlyGrowth = defaultKeyStatistics.get("earningsQuarterlyGrowth", {}).get("raw", "N/A")
                earningsQuarterlyGrowth_fmt = defaultKeyStatistics.get("earningsQuarterlyGrowth", {}).get("fmt", "N/A")
                revenueQuarterlyGrowth = defaultKeyStatistics.get("revenueQuarterlyGrowth", {}).get("raw", "N/A")
                revenueQuarterlyGrowth_fmt = defaultKeyStatistics.get("revenueQuarterlyGrowth", {}).get("fmt", "N/A")
                netIncomeToCommon = defaultKeyStatistics.get("netIncomeToCommon", {}).get("raw", "N/A")
                netIncomeToCommon_fmt = defaultKeyStatistics.get("netIncomeToCommon", {}).get("fmt", "N/A")
                netIncomeToCommon_long = defaultKeyStatistics.get("netIncomeToCommon", {}).get("long", "N/A")
                trailingEps = defaultKeyStatistics.get("trailingEps", {}).get("raw", "N/A")
                trailingEps_fmt = defaultKeyStatistics.get("trailingEps", {}).get("fmt", "N/A")
                fowardEps = defaultKeyStatistics.get("forwardEps", {}).get("raw", "N/A")
                fowardEps_fmt = defaultKeyStatistics.get("forwardEps", {}).get("fmt", "N/A")
                pegRatio = defaultKeyStatistics.get("pegRatio", {}).get("raw", "N/A")
                pegRatio_fmt = defaultKeyStatistics.get("pegRatio", {}).get("fmt", "N/A")
                lastSplitFactor = defaultKeyStatistics.get("lastSplitFactor", "N/A")
                lastSplitDate = defaultKeyStatistics.get("lastSplitDate", {}).get("raw", "N/A")
                lastSplitDate_fmt = defaultKeyStatistics.get("lastSplitDate", {}).get("fmt", "N/A")
                enterpriseToRevenue = defaultKeyStatistics.get("enterpriseToRevenue", {}).get("raw", "N/A")
                enterpriseToRevenue_fmt = defaultKeyStatistics.get("enterpriseToRevenue", {}).get("fmt", "N/A")
                enterpriseToEbitda = defaultKeyStatistics.get("enterpriseToEbitda", {}).get("raw", "N/A")
                enterpriseToEbitda_fmt = defaultKeyStatistics.get("enterpriseToEbitda", {}).get("fmt", "N/A")
                fiftyTwoWeekChange = defaultKeyStatistics.get("52WeekChange", {}).get("raw", "N/A")
                fiftyTwoWeekChange_fmt = defaultKeyStatistics.get("52WeekChange", {}).get("fmt", "N/A")
                SandP52WeekChange = defaultKeyStatistics.get("SandP52WeekChange", {}).get("raw", "N/A")
                SandP52WeekChange_fmt = defaultKeyStatistics.get("SandP52WeekChange", {}).get("fmt", "N/A")
                lastDividendValue = defaultKeyStatistics.get("lastDividendValue", {}).get("raw", "N/A")
                lastDividendValue_fmt = defaultKeyStatistics.get("lastDividendValue", {}).get("fmt", "N/A")
                lastDividendDate = defaultKeyStatistics.get("lastDividendValue", {}).get("raw", "N/A")
                lastDividendDate_fmt = defaultKeyStatistics.get("lastDividendValue", {}).get("fmt", "N/A")
                lastCapGain = defaultKeyStatistics.get("lastCapGain", {}).get("raw", "N/A")
                lastCapGain_fmt = defaultKeyStatistics.get("lastCapGain", {}).get("fmt", "N/A")
                annualHoldingsTurnover = defaultKeyStatistics.get("annualHoldingsTurnover", {}).get("raw", "N/A")
                annualHoldingsTurnover_fmt = defaultKeyStatistics.get("annualHoldingsTurnover", {}).get("fmt", "N/A")

                # Create a dictionary of the default key statistics {"enterpriseValue": enterpriseValue_fmt, "fowardPE": fowardPE_fmt, "profitMargins": profitMargins_fmt, "floatShares": floatShares_fmt, "sharesOutstanding": sharesOutstanding_fmt, "sharesShort": sharesShort_fmt, "sharesShortPriorMonth": sharesShortPriorMonth_fmt, "sharesShortPriorMonthDate": sharesShortPriorMonthDate_fmt, "enterpriseToRevenue": enterpriseToRevenue_fmt, "enterpriseToEbitda": enterpriseToEbitda_fmt, "52WeekChange": fiftyTwoWeekChange_fmt, "SandP52WeekChange": SandP52WeekChange_fmt, "lastDividendValue": lastDividendValue_fmt, "lastCapGain": lastCapGain_fmt, "annualHoldingsTurnover": annualHoldingsTurnover_fmt}
                defaultKeyStatistics_data = {"enterpriseValue": enterpriseValue_fmt, "totalAssets": totalAssets_fmt, "legalType": legalType, "fundFamily": fundFamily, "fundInceptionDate": fundInceptionDate, "yieldOverall": yieldOverall, "forwardPE": forwardPE_fmt, "profitMargins": profitMargins_fmt, "heldPercentInsiders": heldPercentInsiders_fmt, "heldPercentInstitutions": heldPercentInstitutions_fmt, "floatShares": floatShares_fmt, "impliedSharesOut": impliedSharesOutstanding_fmt,"sharesOutstanding": sharesOutstanding_fmt, "sharesPercentSharesOut": sharesPercentSharesOut_fmt, "shortRatio": shortRatio_fmt, "sharesShort": sharesShort_fmt, "sharesShortPriorMonth": sharesShortPriorMonth_fmt, "sharesShortPriorMonthDate": sharesShortPriorMonthDate_fmt, "priorMonthDateShortInterest":dateShortInterest_fmt,"enterpriseToRevenue": enterpriseToRevenue_fmt, "enterpriseToEbitda": enterpriseToEbitda_fmt, "52WeekChange": fiftyTwoWeekChange_fmt, "SandP52WeekChange": SandP52WeekChange_fmt, "beta": beta_fmt, "beta3Year": beta3Year_fmt, "bookValue": bookValue_fmt, "priceToBook": priceToBook_fmt, "ytdReturn": ytdReturn_fmt, "threeYearAverageReturn": threeYearAverageReturn_fmt, "fiveYearAverageReturn": fiveYearAverageReturn_fmt, "netIncomeToCommon": netIncomeToCommon_fmt, "earningsQuarterlyGrowth": earningsQuarterlyGrowth_fmt, "revenueQuarterlyGrowth": revenueQuarterlyGrowth_fmt, "trailingEPS": trailingEps_fmt, "fowardEPS": fowardEps_fmt, "lastDividendValue": lastDividendValue_fmt, "lastDividendDate": lastDividendDate_fmt, "lastCapGain": lastCapGain_fmt, "mostRecentQuarter": mostRecentQuarter_fmt, "lastFiscalYearEnd": lastFiscalYearEnd_fmt, "nextFiscalYearEnd": nextFiscalYearEnd_fmt, "lastSplitFactor": lastSplitFactor, "lastSplitDate": lastSplitDate_fmt, "annualReportExpenseRatio": annualReportExpenseRatio_fmt,"annualHoldingsTurnover": annualHoldingsTurnover_fmt}

                # get a list of financial data
                financials = response_data['financialData']
                currentPrice = financials.get("currentPrice", {}).get("raw", "N/A")
                currentPrice_fmt = financials.get("currentPrice", {}).get("fmt", "N/A")
                targetHighPrice = financials.get("targetHighPrice", {}).get("raw", "N/A")
                targetHighPrice_fmt = financials.get("targetHighPrice", {}).get("fmt", "N/A")
                targetLowPrice = financials.get("targetLowPrice", {}).get("raw", "N/A")
                targetLowPrice_fmt = financials.get("targetLowPrice", {}).get("fmt", "N/A")
                targetMeanPrice = financials.get("targetMeanPrice", {}).get("raw", "N/A")
                targetMeanPrice_fmt = financials.get("targetMeanPrice", {}).get("fmt", "N/A")
                targetMedianPrice = financials.get("targetMedianPrice", {}).get("raw", "N/A")
                targetMedianPrice_fmt = financials.get("targetMedianPrice", {}).get("fmt", "N/A")
                recommendationMean = financials.get("recommendationMean", {}).get("raw", "N/A")
                recommendationMean_fmt = financials.get("recommendationMean", {}).get("fmt", "N/A")
                recomendationKey = financials.get("recommendationKey", "N/A")
                numberOfAnalystOpinions = financials.get("numberOfAnalystOpinions", {}).get("raw", "N/A")
                totalCash = financials.get("totalCash", {}).get("raw", "N/A")
                totalCash_fmt = financials.get("totalCash", {}).get("fmt", "N/A")
                totalCash_long = financials.get("totalCash", {}).get("longFmt", "N/A")
                totalCashPerShare = financials.get("totalCashPerShare", {}).get("raw", "N/A")
                totalCashPerShare_fmt = financials.get("totalCashPerShare", {}).get("fmt", "N/A")
                ebitda = financials.get("ebitda", {}).get("raw", "N/A")
                ebitda_fmt = financials.get("ebitda", {}).get("fmt", "N/A")
                ebitda_long = financials.get("ebitda", {}).get("longFmt", "N/A")
                totalDebt = financials.get("totalDebt", {}).get("raw", "N/A")
                totalDebt_fmt = financials.get("totalDebt", {}).get("fmt", "N/A")
                totalDebt_long = financials.get("totalDebt", {}).get("longFmt", "N/A")
                quickRatio = financials.get("quickRatio", {}).get("raw", "N/A")
                quickRatio_fmt = financials.get("quickRatio", {}).get("fmt", "N/A")
                currentRatio = financials.get("currentRatio", {}).get("raw", "N/A")
                currentRatio_fmt = financials.get("currentRatio", {}).get("fmt", "N/A")
                totalRevenue = financials.get("totalRevenue", {}).get("raw", "N/A")
                totalRevenue_fmt = financials.get("totalRevenue", {}).get("fmt", "N/A")
                totalRevenue_long = financials.get("totalRevenue", {}).get("longFmt", "N/A")
                debtToEquity = financials.get("debtToEquity", {}).get("raw", "N/A")
                debtToEquity_fmt = financials.get("debtToEquity", {}).get("fmt", "N/A")
                revenuePerShare = financials.get("revenuePerShare", {}).get("raw", "N/A")
                revenuePerShare_fmt = financials.get("revenuePerShare", {}).get("fmt", "N/A")
                returnOnAssets = financials.get("returnOnAssets", {}).get("raw", "N/A")
                returnOnAssets_fmt = financials.get("returnOnAssets", {}).get("fmt", "N/A")
                returnOnEquity = financials.get("returnOnEquity", {}).get("raw", "N/A")
                returnOnEquity_fmt = financials.get("returnOnEquity", {}).get("fmt", "N/A")
                grossProfits = financials.get("grossProfits", {}).get("raw", "N/A")
                grossProfits_fmt = financials.get("grossProfits", {}).get("fmt", "N/A")
                grossProfits_long = financials.get("grossProfits", {}).get("longFmt", "N/A")
                freeCashflow = financials.get("freeCashflow", {}).get("raw", "N/A")
                freeCashflow_fmt = financials.get("freeCashflow", {}).get("fmt", "N/A")
                freeCashflow_long = financials.get("freeCashflow", {}).get("longFmt", "N/A")
                operatingCashflow = financials.get("operatingCashflow", {}).get("raw", "N/A")
                operatingCashflow_fmt = financials.get("operatingCashflow", {}).get("fmt", "N/A")
                operatingCashflow_long = financials.get("operatingCashflow", {}).get("longFmt", "N/A")
                earningsGrowth = financials.get("earningsGrowth", {}).get("raw", "N/A")
                earningsGrowth_fmt = financials.get("earningsGrowth", {}).get("fmt", "N/A")
                revenueGrowth = financials.get("revenueGrowth", {}).get("raw", "N/A")
                revenueGrowth_fmt = financials.get("revenueGrowth", {}).get("fmt", "N/A")
                grossMargins = financials.get("grossMargins", {}).get("raw", "N/A")
                grossMargins_fmt = financials.get("grossMargins", {}).get("fmt", "N/A")
                ebitdaMargins = financials.get("ebitdaMargins", {}).get("raw", "N/A")
                ebitdaMargins_fmt = financials.get("ebitdaMargins", {}).get("fmt", "N/A")
                operatingMargins = financials.get("operatingMargins", {}).get("raw", "N/A")
                operatingMargins_fmt = financials.get("operatingMargins", {}).get("fmt", "N/A")
                profitMargins = financials.get("profitMargins", {}).get("raw", "N/A")
                profitMargins_fmt = financials.get("profitMargins", {}).get("fmt", "N/A")
                financialCurrency = financials.get("financialCurrency", "N/A")
                # create a dictionary of the financials
                financials_data = {"currentPrice": currentPrice_fmt, "targetLowPrice": targetLowPrice_fmt, "targetHighPrice": targetHighPrice_fmt, "targetMeanPrice": targetMeanPrice_fmt, "targetMedianPrice": targetMedianPrice_fmt, "recommendationMean": recommendationMean_fmt, "recomendationKey": recomendationKey, "numberOfAnalystOpinions": numberOfAnalystOpinions, "totalCash": totalCash_fmt, "totalCashPerShare": totalCashPerShare_fmt, "ebitda": ebitda_fmt, "totalDebt": totalDebt_fmt, "quickRatio": quickRatio_fmt, "currentRatio": currentRatio_fmt, "totalRevenue": totalRevenue_fmt, "debtToEquity": debtToEquity_fmt, "revenuePerShare": revenuePerShare_fmt, "returnOnAssets": returnOnAssets_fmt, "returnOnEquity": returnOnEquity_fmt, "grossProfits": grossProfits_fmt, "freeCashflow": freeCashflow_fmt, "operatingCashflow": operatingCashflow_fmt, "earningsGrowth": earningsGrowth_fmt, "revenueGrowth": revenueGrowth_fmt, "grossMargins": grossMargins_fmt, "ebitdaMargins": ebitdaMargins_fmt, "operatingMargins": operatingMargins_fmt, "profitMargins": profitMargins_fmt, "financialCurrency": financialCurrency}

                # Get the incomeStatementHistoryQuarterly
                quarterlyIncomeStatements = []
                incomeStatementHistoryQuarterly = response_data.get("incomeStatementHistoryQuarterly", {}).get("incomeStatementHistory", "N/A")
                for quarterlyIncome in incomeStatementHistoryQuarterly:
                        endDate = quarterlyIncome.get("endDate", {}).get("raw", "N/A")
                        endDate_fmt = quarterlyIncome.get("endDate", {}).get("fmt", "N/A")
                        totalRevenue = quarterlyIncome.get("totalRevenue", {}).get("raw", "N/A")
                        totalRevenue_fmt = quarterlyIncome.get("totalRevenue", {}).get("fmt", "N/A")
                        totalRevenue_long = quarterlyIncome.get("totalRevenue", {}).get("longFmt", "N/A")
                        costOfRevenue = quarterlyIncome.get("costOfRevenue", {}).get("raw", "N/A")
                        costOfRevenue_fmt = quarterlyIncome.get("costOfRevenue", {}).get("fmt", "N/A")
                        costOfRevenue_long = quarterlyIncome.get("costOfRevenue", {}).get("longFmt", "N/A")
                        grossProfit = quarterlyIncome.get("grossProfit", {}).get("raw", "N/A")
                        grossProfit_fmt = quarterlyIncome.get("grossProfit", {}).get("fmt", "N/A")
                        grossProfit_long = quarterlyIncome.get("grossProfit", {}).get("longFmt", "N/A")
                        researchDevelopment = quarterlyIncome.get("researchDevelopment", {}).get("raw", "N/A")
                        researchDevelopment_fmt = quarterlyIncome.get("researchDevelopment", {}).get("fmt", "N/A")
                        researchDevelopment_long = quarterlyIncome.get("researchDevelopment", {}).get("longFmt", "N/A")
                        sellingGeneralAdministrative = quarterlyIncome.get("sellingGeneralAdministrative", {}).get("raw", "N/A")
                        sellingGeneralAdministrative_fmt = quarterlyIncome.get("sellingGeneralAdministrative", {}).get("fmt", "N/A")
                        sellingGeneralAdministrative_long = quarterlyIncome.get("sellingGeneralAdministrative", {}).get("longFmt", "N/A")
                        nonRecurring = quarterlyIncome.get("nonRecurring", {}).get("raw", "N/A")
                        nonRecurring_fmt = quarterlyIncome.get("nonRecurring", {}).get("fmt", "N/A")
                        nonRecurring_long = quarterlyIncome.get("nonRecurring", {}).get("longFmt", "N/A")
                        otherOperatingExpenses = quarterlyIncome.get("otherOperatingExpenses", {}).get("raw", "N/A")
                        otherOperatingExpenses_fmt = quarterlyIncome.get("otherOperatingExpenses", {}).get("fmt", "N/A")
                        otherOperatingExpenses_long = quarterlyIncome.get("otherOperatingExpenses", {}).get("longFmt", "N/A")
                        totalOperatingExpenses = quarterlyIncome.get("totalOperatingExpenses", {}).get("raw", "N/A")
                        totalOperatingExpenses_fmt = quarterlyIncome.get("totalOperatingExpenses", {}).get("fmt", "N/A")
                        totalOperatingExpenses_long = quarterlyIncome.get("totalOperatingExpenses", {}).get("longFmt", "N/A")
                        operatingIncome = quarterlyIncome.get("operatingIncome", {}).get("raw", "N/A")
                        operatingIncome_fmt = quarterlyIncome.get("operatingIncome", {}).get("fmt", "N/A")
                        operatingIncome_long = quarterlyIncome.get("operatingIncome", {}).get("longFmt", "N/A")
                        totalOtherIncomeExpensesNet = quarterlyIncome.get("totalOtherIncomeExpensesNet", {}).get("raw", "N/A")
                        totalOtherIncomeExpensesNet_fmt = quarterlyIncome.get("totalOtherIncomeExpensesNet", {}).get("fmt", "N/A")
                        totalOtherIncomeExpensesNet_long = quarterlyIncome.get("totalOtherIncomeExpensesNet", {}).get("longFmt", "N/A")
                        ebit = quarterlyIncome.get("ebit", {}).get("raw", "N/A")
                        ebit_fmt = quarterlyIncome.get("ebit", {}).get("fmt", "N/A")
                        ebit_long = quarterlyIncome.get("ebit", {}).get("longFmt", "N/A")
                        interestExpense = quarterlyIncome.get("interestExpense", {}).get("raw", "N/A")
                        interestExpense_fmt = quarterlyIncome.get("interestExpense", {}).get("fmt", "N/A")
                        interestExpense_long = quarterlyIncome.get("interestExpense", {}).get("longFmt", "N/A")
                        incomeBeforeTax = quarterlyIncome.get("incomeBeforeTax", {}).get("raw", "N/A")
                        incomeBeforeTax_fmt = quarterlyIncome.get("incomeBeforeTax", {}).get("fmt", "N/A")
                        incomeBeforeTax_long = quarterlyIncome.get("incomeBeforeTax", {}).get("longFmt", "N/A")
                        incomeTaxExpense = quarterlyIncome.get("incomeTaxExpense", {}).get("raw", "N/A")
                        incomeTaxExpense_fmt = quarterlyIncome.get("incomeTaxExpense", {}).get("fmt", "N/A")
                        incomeTaxExpense_long = quarterlyIncome.get("incomeTaxExpense", {}).get("longFmt", "N/A")
                        minorityInterest = quarterlyIncome.get("minorityInterest", {}).get("raw", "N/A")
                        minorityInterest_fmt = quarterlyIncome.get("minorityInterest", {}).get("fmt", "N/A")
                        minorityInterest_long = quarterlyIncome.get("minorityInterest", {}).get("longFmt", "N/A")
                        netIncomeFromContinuingOps = quarterlyIncome.get("netIncomeFromContinuingOps", {}).get("raw", "N/A")
                        netIncomeFromContinuingOps_fmt = quarterlyIncome.get("netIncomeFromContinuingOps", {}).get("fmt", "N/A")
                        netIncomeFromContinuingOps_long = quarterlyIncome.get("netIncomeFromContinuingOps", {}).get("longFmt", "N/A")
                        discontinuedOperations = quarterlyIncome.get("discontinuedOperations", {}).get("raw", "N/A")
                        discontinuedOperations_fmt = quarterlyIncome.get("discontinuedOperations", {}).get("fmt", "N/A")
                        discontinuedOperations_long = quarterlyIncome.get("discontinuedOperations", {}).get("longFmt", "N/A")
                        extraordinaryItems = quarterlyIncome.get("extraordinaryItems", {}).get("raw", "N/A")
                        extraordinaryItems_fmt = quarterlyIncome.get("extraordinaryItems", {}).get("fmt", "N/A")
                        extraordinaryItems_long = quarterlyIncome.get("extraordinaryItems", {}).get("longFmt", "N/A")
                        effectOfAccountingCharges = quarterlyIncome.get("effectOfAccountingCharges", {}).get("raw", "N/A")
                        effectOfAccountingCharges_fmt = quarterlyIncome.get("effectOfAccountingCharges", {}).get("fmt", "N/A")
                        effectOfAccountingCharges_long = quarterlyIncome.get("effectOfAccountingCharges", {}).get("longFmt", "N/A")
                        otherItems = quarterlyIncome.get("otherItems", {}).get("raw", "N/A")
                        otherItems_fmt = quarterlyIncome.get("otherItems", {}).get("fmt", "N/A")
                        otherItems_long = quarterlyIncome.get("otherItems", {}).get("longFmt", "N/A")
                        netIncome = quarterlyIncome.get("netIncome", {}).get("raw", "N/A")
                        netIncome_fmt = quarterlyIncome.get("netIncome", {}).get("fmt", "N/A")
                        netIncome_long = quarterlyIncome.get("netIncome", {}).get("longFmt", "N/A")
                        netIncomeApplicableToCommonShares = quarterlyIncome.get("netIncomeApplicableToCommonShares", {}).get("raw", "N/A")
                        netIncomeApplicableToCommonShares_fmt = quarterlyIncome.get("netIncomeApplicableToCommonShares", {}).get("fmt", "N/A")
                        netIncomeApplicableToCommonShares_long = quarterlyIncome.get("netIncomeApplicableToCommonShares", {}).get("longFmt", "N/A")
                        quarterlyIncome_data = {"endDate": endDate_fmt, "totalRevenue": totalRevenue_fmt, "costOfRevenue": costOfRevenue_fmt, "grossProfit": grossProfit_fmt, "researchDevelopment": researchDevelopment_fmt, "sellingGeneralAdministrative": sellingGeneralAdministrative_fmt, "nonRecurring": nonRecurring_fmt, "otherOperatingExpenses": otherOperatingExpenses_fmt, "totalOperatingExpenses": totalOperatingExpenses_fmt, "operatingIncome": operatingIncome_fmt, "totalOtherIncomeExpensesNet": totalOtherIncomeExpensesNet_fmt, "ebit": ebit_fmt, "interestExpense": interestExpense_fmt, "incomeBeforeTax": incomeBeforeTax_fmt, "incomeTaxExpense": incomeTaxExpense_fmt, "minorityInterest": minorityInterest_fmt, "netIncomeFromContinuingOps": netIncomeFromContinuingOps_fmt, "discontinuedOperations": discontinuedOperations_fmt, "extraordinaryItems": extraordinaryItems_fmt, "effectOfAccountingCharges": effectOfAccountingCharges_fmt, "otherItems": otherItems_fmt, "netIncome": netIncome_fmt, "netIncomeApplicableToCommonShares": netIncomeApplicableToCommonShares_fmt}
                        quarterlyIncomeStatements.append(quarterlyIncome_data)

                # get cashflowStatementHistory
                cashflowStatementHistory_list = []
                cashflowStatementHistory = response_data.get("cashflowStatementHistory", {}).get("cashflowStatements", [])
                for cashflowStatement in cashflowStatementHistory:
                        endDate = cashflowStatement.get("endDate", {}).get("raw", "N/A")
                        endDate_fmt = cashflowStatement.get("endDate", {}).get("fmt", "N/A")
                        netIncome = cashflowStatement.get("netIncome", {}).get("raw", "N/A")
                        netIncome_fmt = cashflowStatement.get("netIncome", {}).get("fmt", "N/A")
                        netIncome_long = cashflowStatement.get("netIncome", {}).get("longFmt", "N/A")
                        depreciation = cashflowStatement.get("depreciation", {}).get("raw", "N/A")
                        depreciation_fmt = cashflowStatement.get("depreciation", {}).get("fmt", "N/A")
                        depreciation_long = cashflowStatement.get("depreciation", {}).get("longFmt", "N/A")
                        changeToNetIncome = cashflowStatement.get("changeToNetincome", {}).get("raw", "N/A")
                        changeToNetIncome_fmt = cashflowStatement.get("changeToNetincome", {}).get("fmt", "N/A")
                        changeToNetIncome_long = cashflowStatement.get("changeToNetincome", {}).get("longFmt", "N/A")
                        changeToAccountReceivables = cashflowStatement.get("changeToAccountReceivables", {}).get("raw", "N/A")
                        changeToAccountReceivables_fmt = cashflowStatement.get("changeToAccountReceivables", {}).get("fmt", "N/A")
                        changeToAccountReceivables_long = cashflowStatement.get("changeToAccountReceivables", {}).get("longFmt", "N/A")
                        changeToLiabilities = cashflowStatement.get("changeToLiabilities", {}).get("raw", "N/A")
                        changeToLiabilities_fmt = cashflowStatement.get("changeToLiabilities", {}).get("fmt", "N/A")
                        changeToLiabilities_long = cashflowStatement.get("changeToLiabilities", {}).get("longFmt", "N/A")
                        changeToInventory = cashflowStatement.get("changeToInventory", {}).get("raw", "N/A")
                        changeToInventory_fmt = cashflowStatement.get("changeToInventory", {}).get("fmt", "N/A")
                        changeToInventory_long = cashflowStatement.get("changeToInventory", {}).get("longFmt", "N/A")
                        changeToOperatingActivities = cashflowStatement.get("changeToOperatingActivities", {}).get("raw", "N/A")
                        changeToOperatingActivities_fmt = cashflowStatement.get("changeToOperatingActivities", {}).get("fmt", "N/A")
                        changeToOperatingActivities_long = cashflowStatement.get("changeToOperatingActivities", {}).get("longFmt", "N/A")
                        totalCashFromOperatingActivities = cashflowStatement.get("totalCashFromOperatingActivities", {}).get("raw", "N/A")
                        totalCashFromOperatingActivities_fmt = cashflowStatement.get("totalCashFromOperatingActivities", {}).get("fmt", "N/A")
                        totalCashFromOperatingActivities_long = cashflowStatement.get("totalCashFromOperatingActivities", {}).get("longFmt", "N/A")
                        capitalExpenditures = cashflowStatement.get("capitalExpenditures", {}).get("raw", "N/A")
                        capitalExpenditures_fmt = cashflowStatement.get("capitalExpenditures", {}).get("fmt", "N/A")
                        capitalExpenditures_long = cashflowStatement.get("capitalExpenditures", {}).get("longFmt", "N/A")
                        investments = cashflowStatement.get("investments", {}).get("raw", "N/A")
                        investments_fmt = cashflowStatement.get("investments", {}).get("fmt", "N/A")
                        investments_long = cashflowStatement.get("investments", {}).get("longFmt", "N/A")
                        otherCashflowsFromInvestingActivities = cashflowStatement.get("otherCashflowsFromInvestingActivities", {}).get("raw", "N/A")
                        otherCashflowsFromInvestingActivities_fmt = cashflowStatement.get("otherCashflowsFromInvestingActivities", {}).get("fmt", "N/A")
                        otherCashflowsFromInvestingActivities_long = cashflowStatement.get("otherCashflowsFromInvestingActivities", {}).get("longFmt", "N/A")
                        totalCashflowsFromInvestingActivities = cashflowStatement.get("totalCashflowsFromInvestingActivities", {}).get("raw", "N/A")
                        totalCashflowsFromInvestingActivities_fmt = cashflowStatement.get("totalCashflowsFromInvestingActivities", {}).get("fmt", "N/A")
                        totalCashflowsFromInvestingActivities_long = cashflowStatement.get("totalCashflowsFromInvestingActivities", {}).get("longFmt", "N/A")
                        dividendsPaid = cashflowStatement.get("dividendsPaid", {}).get("raw", "N/A")
                        dividendsPaid_fmt = cashflowStatement.get("dividendsPaid", {}).get("fmt", "N/A")
                        dividendsPaid_long = cashflowStatement.get("dividendsPaid", {}).get("longFmt", "N/A")
                        netBorrowings = cashflowStatement.get("netBorrowings", {}).get("raw", "N/A")
                        netBorrowings_fmt = cashflowStatement.get("netBorrowings", {}).get("fmt", "N/A")
                        netBorrowings_long = cashflowStatement.get("netBorrowings", {}).get("longFmt", "N/A")
                        otherCashflowsFromFinancingActivities = cashflowStatement.get("otherCashflowsFromFinancingActivities", {}).get("raw", "N/A")
                        otherCashflowsFromFinancingActivities_fmt = cashflowStatement.get("otherCashflowsFromFinancingActivities", {}).get("fmt", "N/A")
                        otherCashflowsFromFinancingActivities_long = cashflowStatement.get("otherCashflowsFromFinancingActivities", {}).get("longFmt", "N/A")
                        totalCashFromFinancingActivities = cashflowStatement.get("totalCashFromFinancingActivities", {}).get("raw", "N/A")
                        totalCashFromFinancingActivities_fmt = cashflowStatement.get("totalCashFromFinancingActivities", {}).get("fmt", "N/A")
                        totalCashFromFinancingActivities_long = cashflowStatement.get("totalCashFromFinancingActivities", {}).get("longFmt", "N/A")
                        changeInCash = cashflowStatement.get("changeInCash", {}).get("raw", "N/A")
                        changeInCash_fmt = cashflowStatement.get("changeInCash", {}).get("fmt", "N/A")
                        changeInCash_long = cashflowStatement.get("changeInCash", {}).get("longFmt", "N/A")
                        repurchaseOfStock = cashflowStatement.get("repurchaseOfStock", {}).get("raw", "N/A")
                        repurchaseOfStock_fmt = cashflowStatement.get("repurchaseOfStock", {}).get("fmt", "N/A")
                        repurchaseOfStock_long = cashflowStatement.get("repurchaseOfStock", {}).get("longFmt", "N/A")
                        cashflowStatementHistory_data = {"endDate": endDate_fmt, "netIncome": netIncome_fmt, "depreciation": depreciation_fmt, "changeToNetIncome": changeToNetIncome_fmt, "changeToAccountReceivables": changeToAccountReceivables_fmt, "changeToLiabilities": changeToLiabilities_fmt, "changeToInventory": changeToInventory_fmt, "changeToOperatingActivities": changeToOperatingActivities_fmt, "totalCashFromOperatingActivities": totalCashFromOperatingActivities_fmt, "capitalExpenditures": capitalExpenditures_fmt, "investments": investments_fmt, "otherCashflowsFromInvestingActivities": otherCashflowsFromInvestingActivities_fmt, "totalCashflowsFromInvestingActivities": totalCashflowsFromInvestingActivities_fmt, "dividendsPaid": dividendsPaid_fmt, "netBorrowings": netBorrowings_fmt, "otherCashflowsFromFinancingActivities": otherCashflowsFromFinancingActivities_fmt, "totalCashFromFinancingActivities": totalCashFromFinancingActivities_fmt, "changeInCash": changeInCash_fmt, "repurchaseOfStock": repurchaseOfStock_fmt}
                        cashflowStatementHistory_list.append(cashflowStatementHistory_data)




# Call modules function with a stock ticker
modules("AMZN")

# TODO: Create the ability to specify what modules that you would like to run to gather data
# TODO: Put all modules into their own functions, when you call the five modules, it will sort the data accordingly and create the dictionaries that we need.
# TODO: We have all this data, but we need to figure out what is neccessary to run the strategy
# TODO: Once we have those dictionaries we can send them to strategy.py to run the strategy