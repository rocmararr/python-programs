# -*- coding = utf-8 -*-

import csv
import pymysql.cursors

# DB CONNECTION:

host = input()

connection = pymysql.connect(host = host,
                            user = user,
                            password = password,
                            db = database,
                            charset = charset,
                            cursorclass = pymysql.cursors.DictCursor)

