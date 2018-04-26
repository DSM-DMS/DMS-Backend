from influxdb import InfluxDBClient

from app import app

influx_settings = app.config['INFLUX_DB_SETTINGS']

c = InfluxDBClient(database=influx_settings['db'], password=influx_settings['pw'])

for db in c.get_list_database():
    if db['name'] == influx_settings['db']:
        break
else:
    c.create_database(influx_settings['db'])
