import requests
from bs4 import BeautifulSoup

from datetime import datetime

from abc import ABC, abstractmethod
class Product(ABC):

    def __init__(self, *args):

        # you can create an object by giving a link and collecting data from it
        # or by giving all the atributes as parameters 
        if len(args) == 1:

            self.link = args[0]
            data = self.getData(self.link)
            self.type = ""

            self.name = data[0]
            self.price = data[1]

            self.time = datetime.now().strftime("%H:%M:%S")

        else:
            self.name = args[0]
            self.price = args[1]
            self.time = args[2]
            self.link = args[3]


    def getData(self, link):
        pass

    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price

    def getLink(self):
        return self.link
    
    def getTime(self):
        return self.time

    def toString(self):
        s = "Name: " + self.name + " Price: " + str(self.price) + " Lei Time: " + self.time + " " + self.link
        return s

    def toTuple(self):
        return (self.name, self.price, self.time, self.link)
    
class EmagProduct(Product):

    def __init__(self, link):
        super().__init__(link)
    
    def getData(self, link):
        r = requests.get(link)
        content = r.content

        soup = BeautifulSoup(content, "html.parser")

        name = soup.find("h1", {"class" : "page-title"}).text.strip()
        price = soup.find("p", {"class" : "product-new-price"}).text.strip().replace(" Lei", "")

        return (name, float(price) * 1000)


class FlancoProduct(Product):

    def __init__(self, link):
        super().__init__(link)
    
    def getData(self, link):
        r = requests.get(link)
        content = r.content

        soup = BeautifulSoup(content, "html.parser")

        name = soup.find("span", {"class" : "base"}).text.strip()
        price = (soup.find("span", {"class" : "special-price"})).find("span", {"class" : "price"}).text.replace('.', "").replace(',', '.').replace(" lei", "")

        return (name, float(price))


class CelProduct(Product):

    def __init__(self, link):
        super().__init__(link)
    
    def getData(self, link):
        r = requests.get(link)
        content = r.content

        soup = BeautifulSoup(content, "html.parser")
        name = soup.find("h1", {"id" : "product-name"}).text.strip()
        price = soup.find("span", {"id" : "product-price"}).text

        return (name, float(price))

class CarrefourProduct(Product):

    def __init__(self, link):
        super().__init__(link)
    
    def getData(self, link):
        r = requests.get(link)
        content = r.content

        soup = BeautifulSoup(content, "html.parser")

        name = soup.find("span", {"class" : "base", "data-ui-id" : "page-title-wrapper", "itemprop" : "name"}).text.strip()
        price = soup.find("span", {"class" : "price"}).text.replace("\xa0Lei", "")
        return(name, float(price))