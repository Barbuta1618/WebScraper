import requests
from bs4 import BeautifulSoup

from datetime import datetime

from abc import ABC, abstractmethod
class Product(ABC):

    def __init__(self, link):

        self.link = link
        data = self.getData(link)
        self.type = ""

        self.name = data[0]
        self.price = data[1]

        self.time = datetime.now()

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
        s = "Name: " + self.name + " Price: " + str(self.price) + " Lei Time: " + self.time.strftime("%H:%M:%S") + " " + self.type
        return s
    
class EmagProduct(Product):

    def __init__(self, link):
        super().__init__(link)
        self.type = "Emag"
    
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
        self.type = "Flanco"
    
    def getData(self, link):
        r = requests.get(link)
        content = r.content

        soup = BeautifulSoup(content, "html.parser")

        name = soup.find("span", {"class" : "base"}).text.strip()
        price = soup.find("span", {"class" : "price"}).text.replace(',', '.').replace(" lei", "")

        return (name, float(price))


class CelProduct(Product):

    def __init__(self, link):
        super().__init__(link)
        self.type = "Cel"
    
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
        self.type = "Carrefour"
    
    def getData(self, link):
        r = requests.get(link)
        content = r.content

        soup = BeautifulSoup(content, "html.parser")

        name = soup.find("span", {"class" : "base","data-ui-id" : "page-title-wrapper", "itemprop" : "name"}).text.strip()
        price = soup.find("span", {"class" : "price"}).text.replace("\xa0Lei", "")
        return(name, float(price))