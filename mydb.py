import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='root',
)

# create cursor object-> used to make connections for executing queries
cursor = mydb.cursor()

# create database
cursor.execute('CREATE DATABASE crmdatabase')

print('Database created!')