import requests
import json

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
print(response.text)