import os 
import json 
from datetime import datetime
import sys
import shutil,bz2,getopt 
import time
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def main(argv):
    ti = time.time()
    input_directory = '/data'
    start_date = False
    end_date = False
    opts = []
    
    i = 0
    while i < len(argv):
        argumento = argv[i]
        valor = argv[i + 1] if i + 1 < len(argv) else ''
        if argumento.startswith('--'):
            opts.append((argumento, ''))
        else:
            if argumento.startswith('-') and not valor.startswith('-'):
                opts.append((argumento, valor))
                i += 2
                continue
            elif argumento.startswith('-') and valor.startswith('-') and not valor.startswith('--'):
                pass
        i += 1
    
    for opt, arg in opts:
        if opt == '-d':
            input_directory = arg
        if opt == '-ff':
            end_date = datetime.strptime(arg, "%d-%m-%y")
        if opt == '-fi':
            start_date = datetime.strptime(arg, "%d-%m-%y")
        if opt == '-h':
            hashtagFile = arg


    for opt, arg in opts:
        if opt == '--grt':
            print('Generate retweet graph')
        if opt == '--jrt':
            print('Generate retweet json')
        if opt == '--gm':
            print('Generate mention graph')
        if opt == '--jm':
            print('Generate mention json')
        if opt == '--gcrt':
            print('Generate coretweet graph')
        if opt == '--jcrt':
            print('Generate coretweet json')
    tf = time.time()

    if (rank == 0):
        #print('input_directory: ', input_directory, 'start_date: ', start_date, 'end_date: ', end_date, 'hashtagFile: ', hashtagFile)
        print(tf - ti)
    

if __name__ == "__main__":
    #print ("hello from process ",rank)
    if (rank == 0):
        main(sys.argv[1:])