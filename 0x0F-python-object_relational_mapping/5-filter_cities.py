#!/usr/bin/python3
'''
Module takes name of a state as an arg
and lists all cities of that state
'''


import MySQLdb
from sys import argv

if __name__ == '__main__':

    state_name = argv[4]
    connector = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3], charset='utf8')
    curs = connector.cursor()
    curs.execute('SELECT cities.name FROM cities, states WHERE\
                 states.name = %(state_name)s\
                 AND state_id=states.id ORDER BY cities.id\
                 ASC', {'state_name': state_name})
    table = curs.fetchall()
    cities = ()
    for row in table:
        cities += row
    print(', '.join(cities))
    curs.close()
    connector.close()
