from clubUser import clubUser
from PCardSession import PCardSession
import json
import ast
from Transaction import Transaction
import os
import psycopg2

conn = psycopg2.connect(os.environ['DATABASE_URL'])
cur = conn.cursor()

print("What's your club name?")
name = input()

print("What's your club password?")
passw = input()

#Currently this isn't used anywhere, planning to construct user database
sampleUser = clubUser(name, passw)

print("Card Check Out Date (Please write in YYYY-MM-DD):")
oDate = input()

print("Card Check In Date(Please write in YYYY-MM-DD):")
iDate = input()

currSession = PCardSession(sampleUser.getClubUserName(), sampleUser.getClubUserPass(), oDate, iDate)

print(currSession)

transactions = currSession.obtainTransaction()

#will be function at some point
with open('isic_cat.json') as f:
    isicData = f.read()
    codesDict = ast.literal_eval(isicData)

for trns in transactions:
    name = trns.get('name')
    code = "0"
    for cat in trns.get('category'):
        if cat in codesDict.keys():
            code = codesDict.get(cat)
    price = trns.get('amount')
    newTransaction = Transaction(name, code, price)

    co2Dict = newTransaction.returnResponse()
    emissions = co2Dict.get('co2e')

    emissions_per_dollar = emissions/price

    cur.execute("""
        INSERT INTO mathclub (name, code, price, emissions, emissions_per_dollar)
        VALUES (%(name)s, %(code)s, %(price)s, %(emissions)s, %(emissions_per_dollar)s);
        """,
        {'name': name, 'code': code, 'price': price, "emissions": emissions, "emissions_per_dollar": emissions_per_dollar})
    conn.commit()

cur.close()
conn.close()
