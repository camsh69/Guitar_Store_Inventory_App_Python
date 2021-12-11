from db.run_sql import run_sql

from models.product import Product
from models.manufacturer import Manufacturer


def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)
