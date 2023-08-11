# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

db = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    passwd = '',
    port = '3306'
)

# prepare a cursore object
cursorObject = db.cursor()

# create a database
cursorObject.execute('CREATE DATABASE crm')

print('Create DB All done')