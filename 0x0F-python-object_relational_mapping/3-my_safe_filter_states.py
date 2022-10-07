#!/usr/bin/python3

'''
    Same script as 2-my_filter_states.py, but
    protects against SQL injections.
'''

import sys
import MySQLdb

if __name__ == '__main__':
    setUp = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3]
    )
    Cursor = setUp.cursor()
    Cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY \
    id ASC", (sys.argv[4],))
    qRows = Cursor.fetchall()
    for r in qRows:
        if r[1] == sys.argv[4]:
            print(r)
    Cursor.close()
    setUp.close()
