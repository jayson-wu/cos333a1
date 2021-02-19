#!/usr/bin/env python

#----------------------------------------------------------------------------------
# testreg.py
# Authors: Connie Xu, Jayson Wu
#----------------------------------------------------------------------------------

import os

def main():

    #reg.py

    # Boundary Tests
    os.system('reg.py')
    os.system('reg.py -d cos -a qr -n 217 -t "Introduction to C_Science Programming Systems"')
    os.system('reg.py -d f')
    os.system('reg.py -d ff')
    os.system('reg.py -d fff')
    os.system('reg.py -d ffff')
    os.system('reg.py -d 123')
    os.system('reg.py -d')
    os.system('reg.py -n abc')
    os.system('reg.py -n 101')
    os.system('reg.py -n 11111')
    os.system('reg.py -n')
    os.system('reg.py -t intro to')
    os.system('reg.py -t 0103')
    os.system('reg.py -o')
    os.system('reg.py a qr')
    os.system('reg.py -A qr')
    os.system('reg.py "-a " qr')
    os.system('reg.py -a qr st')
    os.system('reg.py -a')
    os.system('reg.py -a qr -d')
    os.system('reg.py -a -d cos')
    os.system('reg.py -dd')

    # Statement Tests
    deps = ['aas', 'afs', 'ams', 'ant', 'aos', 'apc', 'ara', 'arc', 'art', 'ast', 'atl', 'cee', 'che', 'chi', 'chm', 'chv', 'cla', 'clg', 'com', 'cos', 'cwr', 'dan', 'eas', 'eco', 'ecs', 'eeb', 'egr', 'ele', 'eng', 'env', 'eps', 'fin', 'fre', 'frs', 'geo', 'ger', 'ghp', 'heb', 'hin', 'his', 'hls', 'hos', 'hum', 'isc', 'ita', 'jds', 'jpn', 'jrn', 'kor', 'lao', 'las', 'lat', 'lin', 'mae', 'mat', 'mol', 'mse', 'mus', 'nes', 'neu', 'orf', 'per', 'phi', 'phy', 'pol', 'pop', 'por', 'psy', 'qcb', 'rel', 'rus', 'sla', 'soc', 'spa', 'swa', 'thr', 'tpp', 'tra', 'tur', 'urb', 'vis', 'wom', 'wri', 'wws', 'paw', 'mog', 'mod', 'med']
    for d in deps:
        os.system('reg.py -d ' + d)
    os.system('reg.py -h')
    os.system('reg.py')
    os.system('reg.py -d COS')
    os.system('reg.py -n 333')
    os.system('reg.py -n b')
    os.system('reg.py -a Qr')
    os.system('reg.py -t intro')
    os.system('reg.py -t science')
    os.system('reg.py -t C_S')
    os.system('reg.py -t c%S')
    os.system('reg.py -d cos -n 3')
    os.system('reg.py -d cos -a qr -n 2 -t intro')
    os.system('reg.py -t "Independent Study"')
    os.system('reg.py -t "Independent Study "')
    os.system('reg.py -t "Independent Study  "')
    os.system('reg.py -t " Independent Study"')
    os.system('reg.py -t "  Independent Study"')
    os.system('reg.py -t=-c')    

#----------------------------------------------------------------------------------
if __name__ == '__main__':
    main()