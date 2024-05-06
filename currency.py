import requests

API_KEY = 'yourApiKeyHere'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
CURRENCIES = ['USD', 'CAD', 'INR', 'AUD', 'CNY']


def convertCurrency(baseCurrency):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={baseCurrency}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    except Exception as e:
        print('Invalid Currency')
        return None


while True:
    base = input('Enter base currency (press Q to quit) : ').upper()

    if base == "Q":
        break

    data = convertCurrency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")
