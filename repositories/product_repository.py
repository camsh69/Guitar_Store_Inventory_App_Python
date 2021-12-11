from db.run_sql import run_sql

from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository


def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)


def save(product):
    sql = "INSERT INTO products (item, description, category, stock_quantity, buying_cost, selling_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.item, product.description, product.category, product.stock_quantity,
              product.buying_cost, product.selling_price, product.manufacturer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return id


def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(
            row['manufacturer_id'])
        product = Product(row['item'], row['description'], row['category'], row['stock_quantity'],
                          row['buying_cost'], row['selling_price'], manufacturer, row['id'])
        products.append(product)
    return products
