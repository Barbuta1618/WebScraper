from os import system
import Products
import DataBase
import time
import os
import json

with open("links.txt", "r") as input:
    emagLink = input.readline().strip()
    flancoLink = input.readline().strip()
    celLink = input.readline().strip()
    carrefourLink = input.readline().strip()

db = DataBase.DataBase('products.db')

def toJSON(minProd, maxProd):
    with open("output.json", "w+", encoding = 'utf-8') as output:
            out = {
                "minName" : minProd[0],
                "minPrice" : minProd[1],
                "minTime" : minProd[2],
                "minLink" : minProd[3],
                "maxName" : maxProd[0],
                "maxPrice" : maxProd[1],
                "maxTime" : maxProd[2],
                "maxLink" : maxProd[3]
            }
            json.dump(out, output, ensure_ascii = False, indent = 4)

def getData():
    while True:
        emagProd = Products.EmagProduct(emagLink)
        flancoProd = Products.FlancoProduct(flancoLink)
        celProd = Products.CelProduct(celLink)
        carrefourProd = Products.CarrefourProduct(carrefourLink)

        db.insertProduct(emagProd.toTuple())
        db.insertProduct(flancoProd.toTuple())
        db.insertProduct(celProd.toTuple())
        db.insertProduct(carrefourProd.toTuple())

        minProd = db.getMinPrice()
        maxProd = db.getMaxPrice()

        os.system("clear")
        print("MinPrice: ")
        print(minProd)
        print("MaxPrice: ")
        print(maxProd)

        toJSON(minProd, maxProd)
    

        time.sleep(3600)
        
getData()