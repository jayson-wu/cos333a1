#!/usr/bin/env python

#----------------------------------------------------------------------------------
# testreg.py
# Authors: Connie Xu, Jayson Wu
#----------------------------------------------------------------------------------

import os


def main():

    # reg.py

    # Boundary Tests
    os.system('python reg.py')
    os.system('python reg.py -d cos -a qr -n 217 -t "Introduction to C_Science Programming Systems"')
    os.system('python reg.py -d f')
    os.system('python reg.py -d ff')
    os.system('python reg.py -d fff')
    os.system('python reg.py -d ffff')
    os.system('python reg.py -d 123')
    os.system('python reg.py -d')
    os.system('python reg.py -n abc')
    os.system('python reg.py -n 101')
    os.system('python reg.py -n 11111')
    os.system('python reg.py -n')
    os.system('python reg.py -t intro to')
    os.system('python reg.py -t 0103')
    os.system('python reg.py -o')
    os.system('python reg.py a qr')
    os.system('python reg.py -A qr')
    os.system('python reg.py "-a " qr')
    os.system('python reg.py -a qr st')
    os.system('python reg.py -a')
    os.system('python reg.py -a qr -d')
    os.system('python reg.py -a -d cos')
    os.system('python reg.py -dd')

    # Statement Tests
    deps = ['aas', 'afs', 'ams', 'ant', 'aos', 'apc', 'ara', 'arc', 'art', 'ast', 'atl', 'cee', 'che', 'chi', 'chm', 'chv', 'cla', 'clg', 'com', 'cos', 'cwr', 'dan', 'eas', 'eco', 'ecs', 'eeb', 'egr', 'ele', 'eng', 'env', 'eps', 'fin', 'fre', 'frs', 'geo', 'ger', 'ghp', 'heb', 'hin', 'his', 'hls', 'hos', 'hum', 'isc', 'ita', 'jds', 'jpn', 'jrn', 'kor', 'lao', 'las', 'lat', 'lin', 'mae', 'mat', 'mol', 'mse', 'mus', 'nes', 'neu', 'orf', 'per', 'phi', 'phy', 'pol', 'pop', 'por', 'psy', 'qcb', 'rel', 'rus', 'sla', 'soc', 'spa', 'swa', 'thr', 'tpp', 'tra', 'tur', 'urb', 'vis', 'wom', 'wri', 'wws', 'paw', 'mog', 'mod', 'med']
    for d in deps:
        os.system('python reg.py -d ' + d)
    os.system('python reg.py -h')
    os.system('python reg.py')
    os.system('python reg.py -d COS')
    os.system('python reg.py -n 333')
    os.system('python reg.py -n b')
    os.system('python reg.py -a Qr')
    os.system('python reg.py -t intro')
    os.system('python reg.py -t science')
    os.system('python reg.py -t C_S')
    os.system('python reg.py -t c%S')
    os.system('python reg.py -d cos -n 3')
    os.system('python reg.py -d cos -a qr -n 2 -t intro')
    os.system('python reg.py -t "Independent Study"')
    os.system('python reg.py -t "Independent Study "')
    os.system('python reg.py -t "Independent Study  "')
    os.system('python reg.py -t " Independent Study"')
    os.system('python reg.py -t "  Independent Study"')
    os.system('python reg.py -t=-c')

    # regdetails.py

    # Boundary
    os.system('python regdetails.py')
    os.system('python regdetails.py 8321 9032')
    os.system('python regdetails.py abc123')
    os.system('python regdetails.py 9034')

    # Statement
    classids = [7865, 7901, 7941, 7932, 7999, 8035, 8327, 8421, 8585, 8877, 8998, 10251, 10111, 10091, 9984, 9819, 9752, 9615, 9572, 9440, 9305]
    for cid in classids:
        os.system('python regdetails.py ' + str(cid))
    os.system('python regdetails.py 8321')
    os.system('python regdetails.py 9032')
    os.system('python regdetails.py 9977')
    os.system('python regdetails.py 9012')
    os.system('python regdetails.py 10188')
    


#----------------------------------------------------------------------------------
if __name__ == '__main__':
    main()