#!/usr/bin/python3
'''
Module does task 2 but safe from an sql injection
'''


import MySQLdb
from sys import argv

if __name__ == '__main__':

    state_name = argv[4]
    connector = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3], charset='utf8')
    curs = connector.cursor()
    curs.execute('SELECT * FROM states WHERE name = %(state_name)s ORDER\
                 BY id ASC', {'state_name': state_name})
    table = curs.fetchall()
    for row in table:
        print(row)
    curs.close()
    connector.close()
