# from controllers.manufacturers_controller import manufacturers
from db.run_sql import run_sql

from models.manufacturer import Manufacturer


def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)


def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, is_active) VALUES (%s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.is_active]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer


def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['is_active'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers


def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(
            result['name'], result['is_active'], result['id'])
    return manufacturer


def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, is_active) = (%s, %s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.is_active, manufacturer.id]
    run_sql(sql, values)