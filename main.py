import os
import multiprocessing

arquivos = ('keylogger.py', 'timer.py')

def Main(arquivo):
    os.system(f'python3 {arquivo}')

pool = multiprocessing.Pool(processes=2)
pool.map(Main, arquivos)
