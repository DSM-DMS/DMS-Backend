from influxdb import InfluxDBClient

from app import app

c = InfluxDBClient(database=app.config['INFLUX_DB_SETTINGS']['db'])