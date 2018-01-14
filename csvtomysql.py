# -*- coding = utf-8 -*-

import csv
import pymysql.cursors


# DB CONNECTION:

#  User information introduction:

print("-----------------------------------------------------------------\n\
Welcome to the CSV to MySQL program. MySQL must be running to make this program work.\n\
You have to write the following fields to insert the data into an existing database.")

host = input("Host: ")
user = input("User: ")
password = input("Password: ")
database = input("Database name: ")
charset = input("Charset (default value is UTF8mb4): ")

if charset == '':
    charset = 'utf8mb4'

#  User confirmation:


connectiondata = {"Host": host, "User": user, "Password": password, \
"Database name": database, "Charset": charset}

print("This is the information you wrote. Please check it before trying to connect:\n\
-----------------")

for key,value in connectiondata.items():
    print("%s: %s" % (key,value))

print("-----------------")

check = input("Do you confirm the information above and want to proceed with the connection? (Y/N): ")

#  Connection with the database:

if check == "Y" or check == "y":
    try:
        connection = pymysql.connect(host = host,
                                user = user,
                                password = password,
                                db = database,
                                charset = charset,
                                cursorclass = pymysql.cursors.DictCursor)
        print("Connection succeeded.")

    except:
        print("\nThere was an error trying to connect to the database. Please, check that the information was correct, restart the program and try again.")
else:
    print("\nPlease restart the program and write the database information again.")

print("-----------------------------------------------------------------")



# CSV LOAD:



# DATABASE STRUCTURE CREATION: