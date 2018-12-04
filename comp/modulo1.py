# 1° modulo manual-geral
import os
import sys
import time

def mts():
    print('...Instalando Metasploit...')
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/rapid7/metasploit-framework')
    os.system('mv metasploit-framework ~ ')
    print('Terminado!!!')
    menu()
def sqlmap():
    print('...Instalando sqlmap...')
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/sqlmapproject/sqlmap')
    os.system('mv sqlmap ~ ')
    print('Terminado!!!')
    menu()
def xerxesin():
    print('...Instalando xerxes...')
    os.system('apt upadte && apt upgrade')
    os.system('apt install git')
    os.system('apt install clang')
    os.system('git clone https://github.com/zanyarjamal/xerxes')
    os.system('cd ~ / xerxes && clang xerxes.c -o xerxes')
    print('Terminado!!!')
    menu()

