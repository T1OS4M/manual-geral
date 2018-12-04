# 1° modulo manual-geral
import os
import sys
import time
def menu():
    print('[01]METASPLOIT')
    time.sleep(0.5)
    print('[02]SQLMAP')
    time.sleep(0.5)
    print('[03]XERXES')
    time.sleep(0.5)
    print('[04]COMANDOS DO TERMUX')
    time.sleep(0.5)
    print('[00]SAIR')
    time.sleep(0.5)
    n = int(input('\n mnl: \n'))
    if n == 1 or n == '01':
        metasploit()
    elif n == 2 or n == '02':
        sql()
    elif n == 3 or n == '03':
        xerxes()
    elif n == 4 or n == '04':
        termux()
    elif n == 00:
        sys.exit()
    else:
        print('\033[31m OPÇÃO INVALIDA \033[m \n')
        menu()
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

