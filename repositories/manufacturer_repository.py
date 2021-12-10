from db.run_sql import run_sql

from models.manufacturer import Manufacturer


def delete_all():
    sql = "DELETE * FROM manufacturers"
    run_sql(sql)
