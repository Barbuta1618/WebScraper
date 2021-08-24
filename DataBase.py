import sqlite3

class DataBase():
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

        createCommand = """ CREATE TABLE IF NOT EXISTS
        products(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, time TEXT, link TEXT)"""

        self.cursor.execute(createCommand)
    
    def insertProduct(self, product):

        oldPrice = self.getPriceByLink(product[3])

        if oldPrice != product[2]:

            insertCommand = "INSERT INTO products VALUES (NULL, '{}', {}, '{}', '{}')"
            self.cursor.execute(insertCommand.format(product[0], product[1], product[2], product[3]))

            self.connection.commit()

    def getPriceByLink(self, link):

        try:
            searchCommand = "SELECT price FROM products WHERE link = ?"
            self.cursor.execute(searchCommand, (link,))
            price = self.cursor.fetchall()[-1]
        except:
            price = -1

        return price
    
    # returns a tuple (name, price, time, link)
    def getMinPrice(self):
        command = " SELECT name, price, time, link FROM products WHERE price = (SELECT min(price) FROM products)"
        self.cursor.execute(command)
        data = self.cursor.fetchall()[-1]

        return data

    def getMaxPrice(self):
        command = " SELECT name, price, time, link FROM products WHERE price = (SELECT max(price) FROM products)"
        self.cursor.execute(command)
        data = self.cursor.fetchall()[-1]

        return data

        