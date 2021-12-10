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
