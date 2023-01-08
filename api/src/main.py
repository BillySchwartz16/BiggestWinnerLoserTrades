from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gainers import biggestwinners
import pymongo
import datetime

app = FastAPI()

@app.get("/")
def hello():
    return {"hello":"world"}

@app.get("/gainers")
def gainers():
    gainers = biggestwinners().gainers
    return gainers

@app.get("/insertgainers")
def insertgainers():
    date = datetime.datetime.now().strftime("%m/%d/%Y")
    gainers = biggestwinners().gainers
    myclient = pymongo.MongoClient("mongodb://host.docker.internal:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb[date]
    x = mycol.insert_one(gainers)
    return {"result":str(x.inserted_id)}

@app.get("/gettodaysgainers")
def gettodaysgainers():
    #todays date
    date = datetime.datetime.now().strftime("%m/%d/%Y")
    myclient = pymongo.MongoClient("mongodb://host.docker.internal:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb[date]
    mydoc = mycol.find_one()
    return {"result":str(mydoc)}