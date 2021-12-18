#!/usr/bin/python3
'''
Module returns a list of all the states from a database
'''


import MySQLdb
from sys import argv

if __name__ == '__main__':

    connector = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3], charset='utf8')
    curs = connector.cursor()
    curs.execute('SELECT * FROM states ORDER BY states.id ASC')
    table = curs.fetchall()
    for row in table:
        print(row)
    curs.close()
    connector.close()
