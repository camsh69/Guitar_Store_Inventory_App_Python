from db.run_sql import run_sql

from models.product import Product
from models.manufacturer import Manufacturer


def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)


def save(product):
    sql = "INSERT INTO products (item, description, category, stock_quantity, buying_cost, selling_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.item, product.description, product.category, product.stock_quantity,
              product.buying.cost, product.selling_price, product.manufacturer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return id
