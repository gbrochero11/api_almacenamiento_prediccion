from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASSWORD"]
host = os.environ["MYSQL_HOST"]
database = os.environ["MYSQL_DATABASE"]

DATABASE_CONNECTION_URI = 'postgres://admin:YTeE1sQQzwqgCGDbtOhJD8aTmNx8gpKe@dpg-cjueve15mpss73dmj8i0-a.oregon-postgres.render.com/ecotech_0yqx'
