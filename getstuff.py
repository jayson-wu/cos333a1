from sys import argv
from sqlite3 import connect

def main(argv):
    DATABASE_NAME = 'reg.sqlite'

    connection = connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    stmtStr = 'SELECT classid FROM classes'
    cursor.execute(stmtStr)
    depts = []
    row = cursor.fetchone()
    while row is not None:
        dep = row[0]
        if dep not in depts:
            depts.append(dep)
        row = cursor.fetchone()

    print(depts)
    cursor.close()
    connection.close()

if __name__ == '__main__':
    main(argv)