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
    parser.add_argument('-d', metavar='dept', nargs=1, help='show only those classes whose department contains dept')
    parser.add_argument('-n', metavar='num', nargs=1, help='show only those classes whose course number contains num')
    parser.add_argument('-a', metavar='area', nargs=1, help='show only those classes whose distrib area contains area')
    parser.add_argument('-t', metavar='title', nargs=1, help='show only those classes whose course title contains title')

    args = parser.parse_args()
    print(args)

    wrapper = textwrap.TextWrapper(width=49)

    if not path.isfile(DATABASE_NAME):
        print(argv[0] + ': database reg.sqlite not found', file=stderr)
        exit(1)

    try:
        connection = connect(DATABASE_NAME)
        cursor = connection.cursor()
        # class ID, dept, course num, area, title
        argsused = []
        stmtStr = 'SELECT classid, dept, coursenum, area, title ' + \
            'FROM classes, courses, crosslistings ' + \
            'WHERE courses.courseid = crosslistings.courseid AND classes.courseid = courses.courseid '

        if args.d != None: 
            stmtStr += 'AND crosslistings.dept LIKE ? '
            argsd = args.d[0].replace('%', '~%')
            argsd = args.d[0].replace('_', '~_')
            argsused.append('%' + argsd + '%')
        if args.n != None: 
            stmtStr += 'AND crosslistings.coursenum LIKE ? '
            argsn = args.n[0].replace('%', '~%')
            argsn = args.n[0].replace('_', '~_')
            argsused.append('%' + argsn + '%')
        if args.a != None:
            stmtStr += 'AND courses.area LIKE ? '
            argsa = args.a[0].replace('%', '~%')
            argsa = args.a[0].replace('_', '~_')
            argsused.append('%' + argsa + '%')
        if args.t != None:
            stmtStr += 'AND courses.title LIKE ? '
            argst = args.t[0].replace('%', '~%')
            argst = args.t[0].replace('_', '~_')
            argsused.append('%' + argst + '%')
        if len(argsused) > 0:
            stmtStr += 'ESCAPE "~" '

        stmtStr += 'ORDER BY dept ASC, coursenum ASC, classid ASC'
        cursor.execute(stmtStr, argsused)

        print('ClsId Dept CrsNum Area Title')
        print('----- ---- ------ ---- -----')

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
                    new_title += '\n' + 23 * ' ' + value
            
            print(f'{row[0]:5}  {row[1]:3}   {row[2].rjust(4)}  {row[3].rjust(3)} {new_title}')
            row = cursor.fetchone()
        
        cursor.close()
        connection.close()

    except Exception as e:
        print(argv[0] + ': ' + str(e), file=stderr)
        exit(1)

    

#----------------------------------------------------------------------------------
if __name__ == '__main__':
    main(argv)