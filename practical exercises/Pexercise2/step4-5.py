from productclass import Product
from productclass import Client
from productclass import VIPClient
o1 = Product("tomato",5)
o2 = Product("potato",3)
o3 = Product("pato",2)
client1 = VIPClient("paula","@paula_")
client2 = Client("Mustafa","@mustafa_")
client1.add_to_cart("tomato",5)
client2.add_to_cart("tomato",5)
print(f"costumer:{client1.name},Total to pay: {client1.compute_total()}")
print(f"costumer:{client2.name},Total to pay: {client2.compute_total()}")