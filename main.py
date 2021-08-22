from os import system
import Products
import DataBase
import threading
import time
import os

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

        
        time.sleep(3600)
        