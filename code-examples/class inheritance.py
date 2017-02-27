

class BasicShoppingList:
    def __init__(self, L=[]):
        self.items = [[item,1] for item in L]

    def __str__(self):
        result = ''
        for i, n in self.items:
            result += '{:10s}  x {}\n'.format(i, n) #e.g. 'Apples  x 3\n'
        return result

    def add(self, product, quantity=1):
        products = [i[0] for i in self.items]
        if product in products:
            index = products.index(product)
            self.items[index][1] += quantity
        else:
            self.items.append([product, quantity])


# Alternatively, inherit from list and gain methods like 'sort'.
class ShoppingList(list):
    def __init__(self, L=[]):
        items = [[item,1] for item in L]
        super().__init__(items)

    def __str__(self):
        result = ''
        for i, n in self:
            result += '{:10s}  x {}\n'.format(i, n) #e.g. 'Apples  x 3\n'
        return result

    def add(self, product, quantity=1):
        products = [i[0] for i in self]
        if product in products:
            index = products.index(product)
            self[index][1] += quantity
        else:
            self.append([product, quantity])



bsl = BasicShoppingList(['Pears', 'Apples'])
print(bsl)
bsl.add('Apples', 2)
bsl.add('Sausages', 12)
print(bsl)
#bsl.sort() #Gives error

sl = ShoppingList(['Pears', 'Apples'])
print(sl)
sl.add('Apples', 2)
sl.add('Sausages', 12)
print(sl)
sl.sort()
print(sl)

