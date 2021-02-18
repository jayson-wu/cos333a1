#!/usr/bin/env python

#----------------------------------------------------------------------------------
# reg.py
# Authors: Connie Xu, Jayson Wu
#----------------------------------------------------------------------------------

import argparse
from os import path
from sys import argv, stderr, exit
from sqlite3 import connect

def main(argv):

    DATABASE_NAME = 'reg.sqlite'

    parser = argparse.ArgumentParser(description='Registrar application: show overviews of classes', allow_abbrev=False)
    parser.add_argument('-d', metavar='dept', help='show only those classes whose department contains dept')
    parser.add_argument('-n', metavar='num', help='show only those classes whose course number contains num')
    parser.add_argument('-a', metavar='area', help='show only those classes whose distrib area contains area')
    parser.add_argument('-t', metavar='title', help='show only those classes whose course title contains title')

    args = parser.parse_args()
    print(args)

    if not path.isfile(DATABASE_NAME):
        print('database reg.sqlite not found', file=stderr)
        exit(1)

    try:
        connection = connect(DATABASE_NAME)
        cursor = connection.cursor()

        stmtStr = 'SELECT * FROM classes'

        
        cursor.execute(stmtStr)
        cursor.close()
        connection.close()

    except Exception as e:
        print(e, file=stderr)
        exit(1)

    

#----------------------------------------------------------------------------------
if __name__ == '__main__':
    main(argv)