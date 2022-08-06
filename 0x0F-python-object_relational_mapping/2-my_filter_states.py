#!/usr/bin/python3
"""takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    cur = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8").cursor()
    cur.execute(f"SELECT * FROM states WHERE name LIKE '{argv[4]}' ORDER BY\
                id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
