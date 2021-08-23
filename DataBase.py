import sqlite3
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

            self.connection.commit()

    def getPriceByLink(self, link):

        try:
            searchCommand = "SELECT price FROM products WHERE link = ?"
            self.cursor.execute(searchCommand, (link,))
            price = self.cursor.fetchall()[-1]
        except:
            price = -1

        return price
    
    def getMinPrice(self):
        command = " SELECT * FROM products WHERE price = (SELECT min(price) FROM products)"
        self.cursor.execute(command)
        data = self.cursor.fetchall()[-1]

        return Products.Product(data[1], data[2], data[3], data[4])

    def getMaxPrice(self):
        command = " SELECT * FROM products WHERE price = (SELECT max(price) FROM products)"
        self.cursor.execute(command)
        data = self.cursor.fetchall()[-1]

        return Products.Product(data[1], data[2], data[3], data[4])

        