##### PostgreSQL #####
import psycopg2
import pandas as pd

connection = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="postgres_db",
    user="postgres",
    password="abc123"
)
cursor = connection.cursor()
connection.commit()

query = "select * from schema1.emp"
df = pd.read_sql(query, connection)

query = '''
    CREATE TABLE mobile
    (ID INT PRIMARY KEY NOT NULL,
    MODEL varchar)
'''
cursor.execute(query)
connection.commit()

query = "insert into schema1.emp (id, name) values (1, 'emp1')"
cursor.execute(query)
connection.commit()
cursor.close()


##### SQLite #####
import sqlite3

connection = sqlite3.connect('cars.db')
cursor = connection.cursor()

rows = cursor.execute("select * fom carmodel").fetchall()
print(rows) #list of tuples

cursor.execute("""
    CREATE TABLE mobile
    (ID INT PRIMARY KEY NOT NULL,
    MODEL varchar)
""")

cursor.execute("insert into emp (id, name) values (1, 'emp1')")
cursor.close()


##### MySql #####
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    database='Electronics',
    user='pynative',
    password='pynative@#29'
)
cursor = connection.cursor()

query = "select * from emp"
df = pd.read_sql(query, connection)

query = '''
    CREATE TABLE mobile
    (ID INT PRIMARY KEY NOT NULL,
    MODEL varchar)
'''
cursor.execute(query)
connection.commit()

query = "insert into schema1.emp (id, name) values (1, 'emp1')"
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()


##### Oracle #####
import sqlalchemy

connection_str = "oracle://user1[schema1]:pswd@dbinstance1"
engine = create_engine(connection_str)
connection = engine.connect()

query = "create table table1 as select * from table2"
connection.execute(query)


##### Sql Server #####
import pyodbc
connection = pyodbc.connect("""
    DRIVER = {ODBC Driver 13 for SQL Server};
    SERVER = Server1\dbinstance1;
    DATABASE = db1;
    UID = test123;
    PWD = Welcome123
""")
result = connection.execute("select * from emp")
for row in result:
    print(row.USER_ID)
result.close()
connection.close();


##### MS Access #####
import pyodbc

connection = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=C:\emp.mdb')
cursor = connection.cursor()

cursor.execute("select * from emp")
for row in cursor.fetchall():
    print(row.USER_ID)





JSON

person.json
{"name": "Bob", 
"languages": ["English", "French"]
}

import json

with open('path_to_file/person.json', 'r') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(data)




INI

FILE.INI
default_path = "/path/name/"
default_file = "file.txt"

import configparser

config = configparser.ConfigParser()
config.read('FILE.INI')
print(config['DEFAULT']['path'])     # -> "/path/name/"
config['DEFAULT']['path'] = '/var/shared/'    # update
config['DEFAULT']['default_message'] = 'Hey! help me!!'   # create

with open('FILE.INI', 'w') as configfile:    # save
    config.write(configfile)