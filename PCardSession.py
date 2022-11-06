import random
import plaid
import Transaction
from datetime import datetime
from plaid.api import plaid_api
from plaid.model.transactions_get_request_options import TransactionsGetRequestOptions
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.category import Category
import json
import ast

class PCardSession:

#Begins a "session"
#This is defined as:
#The use of a card-linked plaid account associated with a particular Student Organization during a particular timeframe
    def __init__(self, user, passw, start, end):
        self.user = user
        self.passw = passw
        #Eventually the session number is used to route transactions from the same club to their respective organizations
        self.sessionNum = random.randint(1000,100000000)
        self.start = start
        self.end = end
        self.access_token = 'access-sandbox-178e4195-fa55-47b3-9297-e170cd2c4174'

        #Configuration copy-pasted from Plaid Docs
        configuration = plaid.Configuration(
            host=plaid.Environment.Sandbox,
            api_key={
                'clientId': '6366a8387c2bc000132d202a',
                'secret': '4f82646e3f1c00da54c0762d671279',
            }
        )

        api_client = plaid.ApiClient(configuration)
        client = plaid_api.PlaidApi(api_client)

        self.client = client
#At some point we'd have this session call for an access token instead of hardcoding it in


#This obtains a list of transactions, each their own dictionary (see Plaid API docs for more info)
    def obtainTransaction(self):
        request = TransactionsGetRequest(
            access_token = self.access_token,
            start_date = datetime.strptime(self.start, '%Y-%m-%d').date(),
            end_date = datetime.strptime(self.end, '%Y-%m-%d').date(),
        )
        response = self.client.transactions_get(request)
        transactions = response['transactions']

        return transactions
