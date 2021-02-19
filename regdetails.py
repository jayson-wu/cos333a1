#!/usr/bin/env python

#----------------------------------------------------------------------------------
# regdetails.py
# Authors: Connie Xu, Jayson Wu
#----------------------------------------------------------------------------------

import argparse
import textwrap
from os import path
from sys import argv, stderr, exit
from sqlite3 import connect

def main(argv):

    DATABASE_NAME = 'reg.sqlite'

    parser = argparse.ArgumentParser(description='Registrar application: show details about a class', allow_abbrev=False)
    parser.add_argument('classid', nargs=1, help='the id of the class whose details should be shown')

    wrapper = textwrap.TextWrapper(width=72)
    
    args = parser.parse_args()

    if not path.isfile(DATABASE_NAME):
        print(argv[0] + ': database reg.sqlite not found', file=stderr)
        exit(1)

    try:
        connection = connect(DATABASE_NAME)
        cursor = connection.cursor()
        # courseid, days, starttime, endtime, bldg, roomnum, dept(s), coursenum(s), area, title, descrip, prereqs, and profname(s)
        # classes                                            crosslistings          courses                        coursesprofs -> profs
        stmtStr1 = 'SELECT courseid, days, starttime, endtime, bldg, roomnum ' + \
            'FROM classes WHERE classes.classid = ?'
                
        cursor.execute(stmtStr1, args.classid)
            
        row = cursor.fetchone()
        
        if row is not None:
            courseid = row[0]
            print('Course Id: ' + str(courseid) + '\n')
            print('Days: ' + row[1])
            print('Start time: ' + row[2])
            print('End time: ' + row[3])
            print('Building: ' + row[4])
            print('Room: ' + row[5] + '\n')
        else:
            print(argv[0] + ': no class with classid ' + str(args.classid[0]) + ' exists', file=stderr)
            exit(1) 
        
        stmtStr2 = 'SELECT dept, coursenum, area, title, descrip, prereqs ' + \
            'FROM crosslistings, courses, coursesprofs ' + \
            'WHERE crosslistings.courseid = ? AND courses.courseid = crosslistings.courseid ' + \
            'ORDER BY dept ASC, coursenum ASC'
            
        cursor.execute(stmtStr2, [courseid])

        deptNum = []
        row = cursor.fetchone()

        area = row[2]
        title = row[3]
        description = row[4]
        prereqs = row[5]
        
        while row is not None:
            dn = row[0] + ' ' + row[1]
            if dn not in deptNum:
                deptNum.append(dn)
            row = cursor.fetchone()

        for dn in deptNum:
            print('Dept and Number: ' + dn)

        print('\n'+ 'Area: ' + area + '\n')
        print(wrapper.fill('Title: ' + title) + '\n')
        print(wrapper.fill('Description: ' + description) + '\n')
        print(wrapper.fill('Prerequisites: ' + prereqs) + '\n')
        
        stmtStr3 = 'SELECT profid FROM coursesprofs WHERE courseid = ?'
        cursor.execute(stmtStr3, [courseid])
        
        profid = []
        row = cursor.fetchone()
        while row is not None:
            profid.append(row[0])
            row = cursor.fetchone()
        
        profs = []
        
        for pid in profid:
            stmtStr4 = 'SELECT profname FROM profs WHERE profs.profid = ?'
            cursor.execute(stmtStr4, [pid])
            row = cursor.fetchone()
            profs.append(row[0])
        
        profs.sort()
        for prof in profs:
            print(wrapper.fill('Professor: ' + prof))
        
        cursor.close()
        connection.close()

    except Exception as e:
        print(argv[0] + ': ' + str(e), file=stderr)
        exit(1)

#----------------------------------------------------------------------------------
if __name__ == '__main__':
    main(argv)