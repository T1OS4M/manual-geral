# 1° modulo manual-geral
import os
import sys
import time
def backtomenu():
    os.system('python3 manual.py')
def mts():
    print('\n...Instalando Metasploit...\n')
    time.sleep(1)
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/rapid7/metasploit-framework')
    os.system('mv metasploit-framework ~ ')
    print('\n Terminado!!! \n')
    time.sleep(0.5)
    backtomenu()
def sqlmap():
    print('\n...Instalando sqlmap...\n')
    time.sleep(1)
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/sqlmapproject/sqlmap')
    os.system('mv sqlmap ~ ')
    time.sleep(0.5)
    print('\n Terminado!!! \n')
    backtomenu()   
def xerxesin():
    print('\n...Instalando xerxes...\n')
    time.sleep(1)
    os.system('apt upadte && apt upgrade')
    os.system('apt install git')
    os.system('apt install clang')
    os.system('git clone https://github.com/zanyarjamal/xerxes')
    os.system('cd ~ / xerxes && clang xerxes.c -o xerxes')
    print('\n Terminado!!! \n')
    time.sleep(0.5)
    backtomenu()

