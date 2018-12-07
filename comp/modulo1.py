# 1° modulo manual-geral
import os
import sys
import time
def banner():
    print('\033[34m   _ _ _ _ \033[m\033[31m°   _ _ _ \033[m')
    time.sleep(0.3)
    print('\033[34m      |    |\033[m  | S4M |      ')
    time.sleep(0.3)
    print('\033[34m      |    |\033[m\033[31m  | S4M |\033[m')
    time.sleep(0.3)
    print('      |    |  | S4M |')
    time.sleep(0.3)
    print('\033[31m      |    |  |_S4M_|\033[m')
    time.sleep(0.3)

    print('\n ... \n')
    time.sleep(0.5)
def backtomenu():
    os.system('python3 manual.py')
def mts():
    print('\n\033[36m...Instalando Metasploit...\033[m\n')
    time.sleep(1)
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/rapid7/metasploit-framework')
    os.system('mv metasploit-framework ~ ')
    print('\n \033[36m #####>: Terminado!!! \033[m \n')
    time.sleep(0.5)
    backtomenu()
def sqlmap():
    print('\n\033[36m...Instalando sqlmap...\033[m\n')
    time.sleep(1)
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/sqlmapproject/sqlmap')
    os.system('mv sqlmap ~ ')
    time.sleep(0.5)
    print('\n \033[36m #####>: Terminado!!! \033[m \n')
    backtomenu()
def xerxesin():
    print('\n\033[36m...Instalando xerxes...\033[m\n')
    time.sleep(1)
    os.system('apt upadte && apt upgrade')
    os.system('apt install git')
    os.system('apt install clang')
    os.system('git clone https://github.com/zanyarjamal/xerxes')
    os.system('cd ~ / xerxes && clang xerxes.c -o xerxes')
    os.system('mv xerxes ~ ')
    print('\n \033[36m #####>: Terminado!!! \033[m \n')
    time.sleep(0.5)
    backtomenu()

