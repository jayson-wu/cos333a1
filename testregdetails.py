#!/usr/bin/env python

#----------------------------------------------------------------------------------
# testregdetails.py
# Authors: Connie Xu, Jayson Wu
#----------------------------------------------------------------------------------

import os


def main():

    #regdetails.py

    # Boundary
    os.system('regdetails.py')
    os.system('regdetails.py 8321 9032')
    os.system('regdetails.py abc123')
    os.system('regdetails.py 9034')

    # Statement
    classids = [7865, 7901, 7941, 7932, 7999, 8035, 8327, 8421, 8585, 8877, 8998, 10251, 10111, 10091, 9984, 9819, 9752, 9615, 9572, 9440, 9305]
    for cid in classids:
        os.system('regdetails.py ' + str(cid))
    os.system('regdetails.py 8321')
    os.system('regdetails.py 9032')
    os.system('regdetails.py 9977')
    os.system('regdetails.py 9012')
    os.system('regdetails.py 10188')
    


#----------------------------------------------------------------------------------
if __name__ == '__main__':
    main()