
class Product:

    def __init__(self,name1=None,price = None):
        self.name1 = name1
        self.price = price

    def __str__(self):

        if self.name1 is None:
            return"No name"


        else:
               return  self.name1


    def get_information(self):
        info = f"Product: {self.name1} | Price: {self.price}"
        return info

class Client:
    def __init__(self, name2=None, email=None,):
        self.name = name2
        self.email = email
        self.cart = []


    def add_to_cart(self,product,price):
        product = Product(product,price)
        return self.cart.append(product)


    def compute_total(self):
        total = 0
        for i in range(len(self.cart)):
            self.cart[i]= int(self.cart[i].price)
            total +=  self.cart[i]
        total = str(total) + "$"
        return total

class VIPClient(Client):
    def add_to_cart(self, product, price):
        product = Product(product, price)
        return self.cart.append(product)

    def compute_total(self):
        total = 0
        for i in range(len(self.cart)):
            self.cart[i] = int(self.cart[i].price)
            total += self.cart[i]
        total = f"{int(total - (total*20/100))} $"
        return total


