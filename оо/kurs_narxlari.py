import requests
from datetime import datetime
def getvalut(to_, from_, amount):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_}&from={from_}&amount={amount}"
    payload = {}
    headers= {
      "apikey": "7002774385:AAE0Gh5ssDf9pGe0nsz4lS8yuo3jx30Nrvs"
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code
    result = response.json()

    text = f'''
    Qaysi vatlutadan: {from_}
    Qaysi vatlutaga: {to_}
    Qancha: {amount} {from_}
    1 {from_} = {result['info']['rate']} {to_}
    {amount} {from_} = {result['result']} {to_}
    So'rov qilingan vaqt: {datetime.fromtimestamp(result['info']['timestamp'])}
    '''
    return text






def getsymbols():
    url = "https://api.apilayer.com/exchangerates_data/symbols"
    payload = {}
    headers = {
        "apikey": "7002774385:AAE0Gh5ssDf9pGe0nsz4lS8yuo3jx30Nrvs"
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.json()
    return result['symbols']