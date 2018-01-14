# -*- coding = utf-8 -*-

import csv
#import json
import pymysql.cursors

# DB CONNECTION:

print("-----------------------------------------------------------------\n\
Welcome to the CSV to MySQL program.\n\
You have to write the following fields to insert the data into an existing database.")

host = input("Host: ")
user = input("User: ")
password = input("Password: ")
database = input("Database name: ")
charset = input("Charset (default value is UTF8mb4): ")

if charset == '':
    charset = 'utf8mb4'

connectiondata = {"Host": host, "User": user, "Password": password, \
"Database name": database, "Charset": charset}

print("-----------------------------------------------------------------\
\nLos datos introducidos son los siguientes:")

for key,value in connectiondata.items():
    print("%s: %s" % (key,value))

print("-----------------------------------------------------------------")

'''connection = pymysql.connect(host = host,
                            user = user,
                            password = password,
                            db = database,
                            charset = charset,
                            cursorclass = pymysql.cursors.DictCursor)'''

