#!/usr/bin/env python

#----------------------------------------------------------------------------------
# testreg.pyc
# Authors: Connie Xu, Jayson Wu
#----------------------------------------------------------------------------------

import os


def main():

    # /u/cos333/Asgt1Solution/ref_reg.pyc

    # Boundary Tests
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -d cos -a qr -n 217 -t "Introduction to C_Science Programming Systems"')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -d f')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -d ff')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -d fff')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -d ffff')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -d 123')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -d')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -n abc')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -n 101')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -n 11111')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -n')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -t intro to')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -t 0103')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -o')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc a qr')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -A qr')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc "-a " qr')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -a qr st')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -a')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -a qr -d')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -a -d cos')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -dd')

    # Statement Tests
    deps = ['aas', 'afs', 'ams', 'ant', 'aos', 'apc', 'ara', 'arc', 'art', 'ast', 'atl', 'cee', 'che', 'chi', 'chm', 'chv', 'cla', 'clg', 'com', 'cos', 'cwr', 'dan', 'eas', 'eco', 'ecs', 'eeb', 'egr', 'ele', 'eng', 'env', 'eps', 'fin', 'fre', 'frs', 'geo', 'ger', 'ghp', 'heb', 'hin', 'his', 'hls', 'hos', 'hum', 'isc', 'ita', 'jds', 'jpn', 'jrn', 'kor', 'lao', 'las', 'lat', 'lin', 'mae', 'mat', 'mol', 'mse', 'mus', 'nes', 'neu', 'orf', 'per', 'phi', 'phy', 'pol', 'pop', 'por', 'psy', 'qcb', 'rel', 'rus', 'sla', 'soc', 'spa', 'swa', 'thr', 'tpp', 'tra', 'tur', 'urb', 'vis', 'wom', 'wri', 'wws', 'paw', 'mog', 'mod', 'med']
    for d in deps:
        os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -d ' + d)
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -h')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -d COS')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -n 333')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -n b')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -a Qr')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -t intro')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -t science')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -t C_S')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -t c%S')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -d cos -n 3')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -d cos -a qr -n 2 -t intro')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -t "Independent Study"')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -t "Independent Study "')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -t "Independent Study  "')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -t " Independent Study"')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -t "  Independent Study"')
    os.system('python /u/cos333/Asgt1Solution/ref_reg.pyc -t=-c')

    # /u/cos333/Asgt1Solution/ref_regdetails.pyc

    # Boundary
    os.system('python /u/cos333/Asgt1Solution/ref_regdetails.pyc')
    os.system('python /u/cos333/Asgt1Solution/ref_regdetails.pyc 8321 9032')
    os.system('python /u/cos333/Asgt1Solution/ref_regdetails.pyc abc123')
    os.system('python /u/cos333/Asgt1Solution/ref_regdetails.pyc 9034')

    # Statement
    classids = [7865, 7901, 7941, 7932, 7999, 8035, 8327, 8421, 8585, 8877, 8998, 10251, 10111, 10091, 9984, 9819, 9752, 9615, 9572, 9440, 9305]
    for cid in classids:
        os.system('python /u/cos333/Asgt1Solution/ref_regdetails.pyc ' + str(cid))
    os.system('python /u/cos333/Asgt1Solution/ref_regdetails.pyc 8321')
    os.system('python /u/cos333/Asgt1Solution/ref_regdetails.pyc 9032')
    os.system('python /u/cos333/Asgt1Solution/ref_regdetails.pyc 9977')
    os.system('python /u/cos333/Asgt1Solution/ref_regdetails.pyc 9012')
    os.system('python /u/cos333/Asgt1Solution/ref_regdetails.pyc 10188')
    


#----------------------------------------------------------------------------------
if __name__ == '__main__':
    main()