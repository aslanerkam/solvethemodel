import sys
import os

costs = {'mesai': 20, 'fazlamesai': 26, 'stoktutma': 2, 'eksikurun': 35}


class Product:
    def __init__(self, filename):
        file = open(filename, "r")
        demanddata = [int(x) for x in file.read().split(',')]
        self.demand = demanddata
        self.production = []
        self.overproduction = []
        self.stock = []
        self.negativestock = []



product1 = Product('demand.txt')


def solve(Product, initialvalues = [], overinitialvalues = []):
    Product.production = initialvalues
    Product.overproduction = overinitialvalues
    stockcalculate(Product)
    print(costcalculate(Product))


def stockcalculate(Product):
    for j, pro in enumerate(Product.production):
        if j == 0:
            Product.stock.append(Product.production[j] + Product.overproduction[j] - Product.demand[j])
            Product.negativestock.append(0)
            if Product.stock[j] < 0:
                Product.negativestock[j] = Product.stock[j]
                Product.stock[j] = 0
        else:
            Product.stock.append(
                Product.stock[j - 1] + Product.production[j] + Product.overproduction[j] - Product.demand[j])
            Product.negativestock.append(0)
            if Product.stock[j] < 0:
                Product.negativestock[j] = Product.stock[j]
                Product.stock[j] = 0



def costcalculate(Product):
    cost = 0
    for j, pro in enumerate(Product.production):
        cost = cost + costs['mesai'] * pro + costs['fazlamesai'] * Product.overproduction[j] - costs['eksikurun'] * Product.negativestock[j] + costs['stoktutma'] * Product.stock[j]
    return cost



solve(product1, [8,2,2,1,30,2,3,2], [20,10,10,10,10,10,40,10])


print(product1.demand)
print(product1.stock)
print(product1.negativestock)
