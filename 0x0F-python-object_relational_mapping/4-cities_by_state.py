#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    cur = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8").cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities,\
                states WHERE cities.state_id = states.id ORDER BY cities.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
