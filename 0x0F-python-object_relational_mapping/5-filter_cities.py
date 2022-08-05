#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    cur = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8").cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id\
                = states.id WHERE states.name LIKE %s ORDER BY cities.id",
                (argv[4],))
    query_rows = cur.fetchall()
    flag = 1
    for row in query_rows:
        if flag:
            print(row[0], end='')
            flag = 0
        else:
            print(f", {row[0]}", end='')
    print()
    cur.close()
