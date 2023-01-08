import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import datetime


class biggestwinners:
    def __init__(self):
        #todays date
        self.date = datetime.datetime.now().strftime("%m/%d/%Y")
        self.req = requests.get("https://finance.yahoo.com/gainers/")
        self.soup = BeautifulSoup(self.req.text, 'lxml')
        self.table1 = self.soup.find('table')
        self.headers = []
        for i in self.table1.find_all('th'):
            title = i.text
            self.headers.append(title)
        self.mydata = pd.DataFrame(columns = self.headers)
        for j in self.table1.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text for i in row_data]
            length = len(self.mydata)
            self.mydata.loc[length] = row
        self.myjson = self.mydata.to_json(orient="split")
        self.parsed = json.loads(self.myjson)
        self.mydata= json.dumps(self.parsed['data'])
        self.buys = {}
        for stock in self.parsed['data']:
            self.buys[stock[0]] = stock[2]
        self.gainers = self.buys
# req = requests.get("https://finance.yahoo.com/gainers/")

# soup = BeautifulSoup(req.text, 'lxml')
# soup

# table1 = soup.find('table')
# table1

# headers = []
# for i in table1.find_all('th'):
#  title = i.text
#  headers.append(title)

# mydata = pd.DataFrame(columns = headers)
# for j in table1.find_all('tr')[1:]:
#  row_data = j.find_all('td')
#  row = [i.text for i in row_data]
#  length = len(mydata)
#  mydata.loc[length] = row

# myjson = mydata.to_json(orient="split")

# parsed = json.loads(myjson)
# mydata= json.dumps(parsed['data'])


# buys = {}
# for stock in parsed['data']:
#     buys[stock[0]] = stock[2]

# print(buys)