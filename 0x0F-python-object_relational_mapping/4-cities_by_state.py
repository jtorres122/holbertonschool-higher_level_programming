#!/usr/bin/python3
'''Module lists all cities from the database'''


import MySQLdb
from sys import argv

connector = MySQLdb.connect(host="localhost", port="3306", user=argv[1],
                            passwd=argv[2], db=argv[3], charset="utf8")
curs = connector.cursor()
curs.execute("SELECT cities.id, cities.name, states.name FROM cities,
             states WHERE states.id=state_id ORDER BY cities.id ASC")
table = curs.fetchall()
for row in table:
    print(row)
curs.close()
connector.close()
