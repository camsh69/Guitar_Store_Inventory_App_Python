from db.run_sql import run_sql

from models.manufacturer import Manufacturer


def delete_all():
    sql = "DELETE * FROM manufacturers"
    run_sql(sql)


def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, active) VALUES (%s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer
