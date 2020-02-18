import pymysql
import sqlalchemy
import MySQLdb
import pandas as pd

engine = sqlalchemy.create_engine('mysql+pymysql://root:belinda94@localhost/sakila')
df = pd.read_sql_table('groceries', engine)
df

#Insert into table
import mysql.connector

mydb = mysql.connector.connect(
    
    host="localhost",
    user="root",
    passwd="belinda94",
    database="sakila"
)

mycursor = mydb.cursor()
sql = "INSERT INTO groceries (Chips, Price, Quantity) VALUES (%s, %s, %s)"
val = ("Ghost Pops", "13", "25")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="belinda94",
  database="sakila"
)

mycursor = mydb.cursor()

sql = "INSERT INTO groceries (Chips, Price, Quantity) VALUES (%s, %s, %s)"
val = [
  ('Big Korn Bites', '25', '154'),
  ('Clown', '30', '52'),
  ('Pops', '10', '52'),
  ('Wola Curls', '20', '8'),
  ('Hije Corns', '15', '63'),
  ('Licky naks', '28', '12'),
  ('Hola Hopps', '19', '12'),
  ('Tranquilia', '31', '23'),
  ('Jives Snaaks', '14', '56'),
  ('Diddle daddles', '23', '3'),
  ('Skopas', '28', '98'),
  ('Ama Kip Kip', '18', '10'),
  ('Shwam-Shwam', '25', '96')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

#Create a table

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="belinda94",
  database="sakila"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE sprint3 (item VARCHAR(255), expiry VARCHAR(255))")

#Checking if table exists
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="belinda94",
  database="sakila"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

#Inerting data into table
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="belinda94",
  database="sakila"
)

mycursor = mydb.cursor()

sql = "INSERT INTO sprint3 (item, expiry) VALUES (%s, %s)"
val = [
  ('Lays', '25-04-2020'),
  ('Simba', '30-05-2020'),
  ('Doretos', '1-01-2019'),
  ('Cheese Curls', '2-05-2023'),
  ('Jumping Jacks', '15-04-2020'),
  ('Nik naks', '20-05-2020'),
  ('Coke', '19-06-2025'),
  ('Fanta', '31-12-2026'),
  ('Jive', '14-12-2099'),
  ('Kingsley', '23-09-2020'),
  ('Bar one', '28-06-2054'),
  ('Tex', '18-06-2001'),
  ('Rolo', '25-04-1994')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

#Delete items in table

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="belinda94",
  database="sakila"
)

mycursor = mydb.cursor()

sql = "DELETE FROM groceries WHERE Chips = 'Clown'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

#Altering a table 

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
  )
mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE groceries ADD product_id VARCHAR(50) NOT NULL AFTER Chips;")



