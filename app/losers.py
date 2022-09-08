import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

req = requests.get("https://finance.yahoo.com/losers/")

soup = BeautifulSoup(req.text, 'lxml')
soup

table1 = soup.find('table')
table1

headers = []
for i in table1.find_all('th'):
 title = i.text
 headers.append(title)
 
mydata = pd.DataFrame(columns = headers)
for j in table1.find_all('tr')[1:]:
 row_data = j.find_all('td')
 row = [i.text for i in row_data]
 length = len(mydata)
 mydata.loc[length] = row
 
myjson = mydata.to_json(orient="split")

parsed = json.loads(myjson)
mydata= json.dumps(parsed['data'])


buys = {}
for stock in parsed['data']:
    buys[stock[0]] = stock[2]
    
print(buys)
    
with open('/data/losersbuys.json', 'w') as fp:
    json.dump(buys, fp)
    
totalshares = {}
totalcost = 0.0
for k,v in buys.items():
    totalshares[k] = {"cost":str(float(v) * 100), "shares":100}
for k,v in totalshares.items():
    totalcost += float(v["cost"])
totalshares["totalcost"] = totalcost
    
with open('/data/losershares.json', 'w') as fp:
    json.dump(totalshares, fp)