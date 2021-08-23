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

def getData():
    while True:
        emagProd = Products.EmagProduct(emagLink)
        flancoProd = Products.FlancoProduct(flancoLink)
        celProd = Products.CelProduct(celLink)
        carrefourProd = Products.CarrefourProduct(carrefourLink)

        db.insertProduct(emagProd)
        db.insertProduct(flancoProd)
        db.insertProduct(celProd)
        db.insertProduct(carrefourProd)

        minProd = db.getMinPrice()
        maxProd = db.getMaxPrice()

        os.system("clear")
        print("MinPrice: ")
        print(minProd.toString())
        print("MaxPrice: ")
        print(maxProd.toString())

        
        with open("output.json", "w+", encoding = 'utf-8') as output:
            minProdDict = { "MinPriceProd" : minProd.__dict__}
            maxProdDict = { "MaxPriceProd" : maxProd.__dict__}
            json.dump([minProdDict, maxProdDict], output, ensure_ascii = False, indent = 4)


        time.sleep(3600)
        
getData()