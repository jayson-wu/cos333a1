#!/usr/bin/env python

#----------------------------------------------------------------------------------
# reg.py
# Authors: Connie Xu, Jayson Wu
#----------------------------------------------------------------------------------

import argparse
import textwrap
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

    wrapper = textwrap.TextWrapper(width=51)

    if not path.isfile(DATABASE_NAME):
        print('database reg.sqlite not found', file=stderr)
        exit(1)

    try:
        connection = connect(DATABASE_NAME)
        cursor = connection.cursor()
        # class ID, dept, course num, area, title
        stmtStr = 'SELECT classid, dept, coursenum, area, title ' + \
            'FROM classes, courses, crosslistings ' + \
            'WHERE courses.courseid = crosslistings.courseid AND classes.courseid = courses.courseid ' + \
            'AND ' + \
            'ORDER BY dept ASC, coursenum ASC, classid ASC'
        cursor.execute(stmtStr)

        row = cursor.fetchone()
        while row is not None:
            rowstr = ''
            #classid = row[0]
            #dept = row[1]
            #coursenum = row[2]
            #area = row[3]
            #title = row[4]
            title = wrapper.wrap(row[4])
            new_title = ''
            for index, value in enumerate(title):
                if (index == 0):
                    new_title += value
                else:
                    new_title += '\n'+23*' ' + value
            
            print(f'{row[0]:5}  {row[1]:3}   {row[2].rjust(4)}   {row[3]:2} {new_title}')
            row = cursor.fetchone()
        
        cursor.close()
        connection.close()

    except Exception as e:
        print(e, file=stderr)
        exit(1)

    

#----------------------------------------------------------------------------------
if __name__ == '__main__':
    main(argv)