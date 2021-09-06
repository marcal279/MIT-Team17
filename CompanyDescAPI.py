import requests


def company_info(symbol):
    symbol=symbol.lower()
    api_key="pk_8d58df2349d7433fb665fe5609363dcc"   # replace if credits over
    url="https://cloud.iexapis.com/stable/stock/"+symbol+"/company?token="+api_key    # uses iex cloud

    r=requests.get(url)
    cdata=r.json()
    companyName=str(cdata["companyName"])
    exchange=str(cdata["exchange"])
    industry=str(cdata["industry"])
    description=str(cdata["description"])
    ceo=str(cdata["CEO"])
    employees=str(cdata["employees"])

    total_desc="Name: {}\nExchange: {}\nIndustry: {}\n\nCEO: {}\nNo. of Employees: {}\n\nDescription:\n{}".format(companyName,exchange,industry,ceo,employees,description)
    return total_desc

#company_info("aapl")  to test
