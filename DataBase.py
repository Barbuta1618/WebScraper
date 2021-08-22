import sqlite3
from sqlite3.dbapi2 import Cursor

import Products

class DataBase():
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

        createCommand = """ CREATE TABLE IF NOT EXISTS
        products(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, time TEXT, link TEXT)"""

        self.cursor.execute(createCommand)
    
    def insertProduct(self, product):

        oldPrice = self.getPriceByLink(product.getLink())

        if oldPrice != product.getPrice():

            insertCommand = "INSERT INTO products VALUES (NULL, ?, ?, ?, ?)"
            self.cursor.execute(insertCommand, (product.getName(), product.getPrice(), product.getTime(), product.getLink()))

            #i'm not sure if the program should take data from previous runs
            #self.connection.commit()
    
    def selectAll(self):
        selectAllCommand = "SELECT * FROM products"
        self.cursor.execute(selectAllCommand)
        return self.cursor.fetchall()

    def getProductById(self, id):
        searchCommand = "SELECT * FROM products WHERE id = ?"
        self.cursor.execute(searchCommand, (id,))
        data = self.cursor.fetchall()[0]

        return Products.Product(data[1], data[2], data[3], data[4])

    def getPriceByLink(self, link):

        try:
            searchCommand = "SELECT price FROM products WHERE link = ?"
            self.cursor.execute(searchCommand, (link,))
            price = self.cursor.fetchall()[-1]
        except:
            price = -1

        return price
    
    def getMinPrice(self):
        products = self.selectAll()

        minPrice = float('inf')
        minPriceId = -1
        for item in products:
            if item[2] <= minPrice:
                minPrice = item[2]
                minPriceId = item[0]
        
        return self.getProductById(minPriceId)


    def getMaxPrice(self):
        products = self.selectAll()

        maxPrice = float('-inf')
        maxPriceId = -1
        for item in products:
            if item[2] >= maxPrice:
                maxPrice = item[2]
                maxPriceId = item[0]
        
        return self.getProductById(maxPriceId)

        