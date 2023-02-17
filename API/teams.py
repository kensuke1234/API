import requests

def getteams():
    
    headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
}    
    json_data = {
    'text': 'Hello World',
}

    response = requests.post('',
    headers=headers,
    json=json_data,
}
    data = response.json()