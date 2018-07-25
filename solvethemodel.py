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
        elif Product.stock[j - 1] < 0:
            Product.stock.append(Product.production[j] + Product.overproduction[j] - Product.demand[j])
        else:
            Product.stock.append(
                Product.stock[j - 1] + Product.production[j] + Product.overproduction[j] - Product.demand[j])



def costcalculate(Product):
    cost = 0
    for j, pro in enumerate(Product.production):
        if Product.stock[j] < 0:
            cost = cost + costs['mesai'] * pro + costs['fazlamesai'] * Product.overproduction[j] + costs['eksikurun'] * \
                   Product.stock[j]
        elif Product.stock[j - 1] > 0:
            cost = cost + costs['mesai'] * pro + costs['fazlamesai'] * Product.overproduction[j] + costs['stoktutma'] * \
                   Product.stock[j - 1]
        else:
            cost = cost + costs['mesai'] * pro + costs['fazlamesai'] * Product.overproduction[j]
    return cost



solve(product1, [10,10,10,10,10,10,10,10], [1,2,3,4,5,6,7,8])


print(product1.demand)
print(product1.stock)
