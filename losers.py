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
    
with open('/data/buys.json', 'w') as fp:
    json.dump(buys, fp)