from flask import Flask,render_template,request
import requests
import json
import scraping
import boto3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html",)

@app.route("/index")
def index():
    name = request.args.get("name")
    return render_template("index.html")

@app.route("/second")
def second():
    name = request.args.get("name")
    return render_template("second.html")

@app.route("/third")
def third():
    name = request.args.get("name")
    return render_template("third.html")

@app.route("/forth")
def forth():
    return render_template("forth.html")

@app.route("/five")
def five():
    return render_template("five.html")

@app.route("/chart")
def chart():
    return render_template("chart.html")


# ↓ /通知メール
@app.route("/getmail")
def gettestmail():
    accesskey = ""
    secretkey = ""
    region = ""
    topic_arn = ""
    sns = boto3.resource("sns", aws_access_key_id=accesskey, aws_secret_access_key=secretkey, region_name=region)
    response = sns.Topic(topic_arn).publish(
        Message="残高照会accountId, 301010006101,accountTypeCode 01 accountTypeName 普通預金（有利息）,balance 3129556,previousDayBalance, 3129556残高照会残高照会残高照会残高照会残高照会",
        Subject="残高照会"
        )
    print("response is {}".format(response))
    return render_template("forth.html")


# ↓ /残高照会
@app.route("/scraping")
def getbalances():
    url = "https://api.sunabar.gmo-aozora.com/personal/v1/accounts/balances"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-access-token': ''
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    balance_data = data["balances"][0]
    return render_template("home.html", data=balance_data)

# ↓ /口座一覧照会
@app.route("/kozaichiran")
def getaccounts():
    url = "https://api.sunabar.gmo-aozora.com/personal/v1/accounts"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-access-token': ''
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return render_template("index.html", data=data)

# ↓ /入出金明細照会
@app.route("/nyushitsu")
def gettransactions():
    url = "https://api.sunabar.gmo-aozora.com/personal/v1/accounts/transactions?accountId=301010006101&dateFrom=2022-08-01&dateTo=2022-08-29&nextItemKey=0"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-access-token': ''
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return render_template("second.html", data=data)

# ↓ /振込
@app.route("/furikomi")
def gettransfer(): 
    url = "https://api.sunabar.gmo-aozora.com/personal/v1/transfer/request"
    payload = json.dumps({
    "accountId": "301010006101",
    "transferDesignatedDate": "2023-04-01",
    "transferDateHolidayCode": "1",
    "totalCount": "1",
    "totalAmount": "8888",
    "transfers": [
       {
         "itemId": "1",
         "transferAmount": "8888",
         "beneficiaryBankCode": "0310",
         "beneficiaryBranchCode": "102",
         "accountTypeCode": "1",
         "accountNumber": "0000048",
         "beneficiaryName": "ｽﾅﾊﾞ ﾏｲｶ"
       }
  ]
})

    headers = {
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'x-access-token': ''
}

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    return render_template("third.html", data=data)

# ↓ /Teams通知
@app.route("/teams")
def getteams():
    
    headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
}    
    json_data = {
    'text': '残高照会accountId, 301010006101,accountTypeCode 01 accountTypeName 普通預金（有利息）,balance 3129556,previousDayBalance, 3129556',
}

    response = requests.post(
      '',
       headers=headers,
       json=json_data,
)      
    data = response.json()
    return render_template("five.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)