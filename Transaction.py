import json
import ast
import requests

#Transactions have:
#a name (usually the merchant)
#a code that links them to a Climatiq API "emission factor"
#a dollar amount associated with the transaction, assumed in usd
class Transaction:
    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price

        # This is how the Climatiq API allows for POST requests through Python
        MY_API_KEY="XS4W7S10VJ4NGGN7WMM4F2TEHZ66"

        url = "https://beta3.api.climatiq.io/estimate"
        region = "US"
        parameters = {
            "money": price,
            "money_unit": "usd"
            }

        json_body = {
            "emission_factor": {
                "activity_id": code
            },

            "parameters": parameters
        }
        authorization_headers = {"Authorization": f"Bearer: {MY_API_KEY}"}
        response = requests.post(url, json=json_body, headers=authorization_headers).json()

        self.response = response

    def returnResponse(self):
        return self.response
