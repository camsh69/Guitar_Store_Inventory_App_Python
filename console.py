from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

product_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer1 = Manufacturer('Fender', True)
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer('Gibson', True)
manufacturer_repository.save(manufacturer2)

# print(manufacturer1.name, manufacturer1.is_active, manufacturer1.id)

# print(manufacturer2.name, manufacturer2.is_active, manufacturer2.id)

# manufacturers = manufacturer_repository.select_all()
# for manufacturer in manufacturers:
#     print(manufacturer.name, manufacturer.is_active, manufacturer.id)

product1 = Product('Stratocaster', 'Six string, Sunburst',
                   'Electric Guitar', 6, 450, 500, manufacturer1)
product_repository.save(product1)
product2 = Product('Les Paul', 'Six string, Black',
                   'Electric Guitar', 4, 950, 1100, manufacturer2)
product_repository.save(product2)
product3 = Product('Telecaster', 'Six string, Blonde',
                   'Electric Guitar', 0, 475, 500, manufacturer1)
product_repository.save(product3)
product4 = Product('Twin Reverb Deluxe', 'Silverface, 50 watt',
                   'Amplifier', 5, 990, 1090, manufacturer1)
product_repository.save(product4)
product5 = Product('SG', 'Six string, Red',
                   'Electric Guitar', 5, 750, 890, manufacturer2)
product_repository.save(product5)

# print(product1.item, product1.description, product1.category, product1.stock_quantity,
#       product1.buying_cost, product1.selling_price, product1.manufacturer.name)

# print(product2.item, product2.description, product2.category, product2.stock_quantity,
#       product2.buying_cost, product2.selling_price, product2.manufacturer.name)

# products = product_repository.select_all()
# for product in products:
#     print(product.item, product.description, product.category, product.stock_quantity,
#           product.buying_cost, product.selling_price, product.manufacturer.name, product.id)
