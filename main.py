import Products

with open("links.txt", "r") as input:
    emagLink = input.readline().strip()
    flancoLink = input.readline().strip()
    celLink = input.readline().strip()
    carrefourLink = input.readline().strip()

emagProd = Products.EmagProduct(emagLink)
flancoProd = Products.FlancoProduct(flancoLink)
celProd = Products.CelProduct(celLink)
carrefourProd = Products.CarrefourProduct(carrefourLink)

print(emagProd.toString())
print(flancoProd.toString())
print(celProd.toString())
print(carrefourProd.toString())
