import requests

def scraping():
    url = "https://api.sunabar.gmo-aozora.com/personal/v1/accounts/balances"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-access-token': ''
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
