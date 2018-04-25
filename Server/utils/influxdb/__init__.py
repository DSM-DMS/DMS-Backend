from influxdb import InfluxDBClient

from app import app

db_name = app.config['INFLUX_DB_SETTINGS']['db']

c = InfluxDBClient(database=db_name)

for db in c.get_list_database():
    if db['name'] == db_name:
        break
else:
    c.create_database(db_name)
