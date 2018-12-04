# Copyright (C) 2018
import sys
import time
from comp.modulo1 import *

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


def metasploit():
    while True:
        time.sleep(0.5)
        print('[01]COMANDOS DO ANDROID')
        time.sleep(0.5)
        print('[02]COMANDOS DE AUDIO')
        time.sleep(0.5)
        print('[03]COMANDOS DA WEBCAM')
        time.sleep(0.5)
        print('[04]COMANDOS DA INTERFACE')
        time.sleep(0.5)
        print('[05]COMANDOS DO SISTEMA')
        time.sleep(0.5)
        print('[06]COMANDOS DE REDE')
        time.sleep(0.5)
        print('[07]COMANDOS DO SISTEMA DE ARQUIVOS')
        time.sleep(0.5)
        print('[08]COMANDOS PRINCIPAIS')
        time.sleep(0.5)
        print('[09]INSTALAR O METASPLOIT')
        time.sleep(0.5)
        print('[99]SAIR')
        time.sleep(0.5)
        opc = int(input('msf: \n'))
        if opc == 1 or opc == '01':
            print('''\033[7;36m COMANDOS DO ANDROID \033[m

        Comando          Descrição
        -------          -----------
        activity_start    Inicie uma atividade do Android a partir de uma string Uri
        check_root        Verifique se o dispositivo tem root
        dump_calllog      Obter registro de chamadas
        dump_contacts     Obter lista de contatos
        dump_sms          Obter mensagens sms
        geolocate         Obtenha a latitude atual usando a geolocalização
        hide_app_icon     Ocultar o ícone do aplicativo no iniciador
        interval_collect  Gerenciar recursos de coleta de intervalo
        send_sms          Envia SMS da sessão de destino\033[7;31m |EX: send_sms -d 1122334455 -t 'gaspar3321'|\033[m
        set_audio_mode    Definir o modo de campainha
        sqlite_query      Consultar um banco de dados SQLite do armazenamento
        wakelock          Usado para manter a conexão mesmo que o android atacado entre em standby 
        wlan_geolocate    Obtém a latitude atual usando informações de WLAN \n''')
        elif opc == 2 or opc == '02':
            print('''\033[7;36m COMANDOS DE AUDIO \033[m

        Comando            Descrição
        -------            -----------
        reproduzir         reproduzir um arquivo de áudio no sistema de destino, nada escrito no disco
    ''')
        elif opc == 3 or opc == '03':
            print(''' \033[7;36m COMANDOS DA WEBCAM E MIC \033[m

        Comando         Descrição
        -------         -----------
        record_mic      Grava áudio do microfone padrão por X segundos\033[7;31m |EX: record_mic -d 10|\033[m
        webcam_chat     Iniciar um bate-papo por vídeo\033[7;31m  |EX: webcam_chat -i 2| \033[m
        webcam_list     Lista de webcams  \033[7;31m|EX: USADO PARA OBTER O ID DA CÂMERA|\033[m 
        webcam_snap     Tire um instantâneo da webcam especificada\033[7;31m|EX: webcam_snap -i 2|\033[m
        webcam_stream   Reproduz um fluxo de vídeo da webcam especificada  \033[7;31m|EX: webcam_stream -i 2\033[m \n''')
        elif opc == 4 or opc == '04':
            print('''\033[7;36m COMANDO DE INTERFACE \033[m

        Comando              Descrição
        -------              -----------
        screenshot      Capture uma captura de tela da área de trabalho interativa \n''')
        elif opc == 5 or opc == '05':
            print(''' \033[7;36m COMANDOS DO SISTEMA \033[m

        Comando           Descrição
        -------           -----------
        execute           Execute um comando
        getuid            Obter o usuário que o servidor está executando como
        localtime         Exibe a data e hora locais do sistema de destino
        pgrep             Filtrar processos por nome
        ps                Processos em execução da lista
        shell             Drop into a shell de comando do sistema
        sysinfo           Obtém informações sobre o sistema remoto, como SO \n''')
        elif opc == 6 or opc == '06':
            print('''\033[7;36m COMANDOS DE REDE \033[m

        Comando                Descrição
        -------                -----------
        ifconfig               interfaces de exibição ifconfig
        ipconfig               interfaces de exibição ipconfig
        portfwd                Encaminhar uma porta local para um serviço remoto
        route                  Visualizar e modificar a tabela de roteamento \n''')
        elif opc == 7 or opc == '07':
            print('''\033[7;36m COMANDOS DO SITEMA DE ARQUIVOS \033[m

        Comando         Descrição
        -------         -----------
        cat             Leia o conteúdo de um arquivo na tela
        cd              Entrar em um Diretório ou pasta |EX: cd Downloads
        checksum        Recupera a soma de verificação de um arquivo
        cp              Copiar a origem para o destino
        dir             Listar arquivos (alias para ls)
        download        Baixar um arquivo ou diretório
        edit            Editar um arquivo
        getlwd          Imprimir diretório de trabalho local
        getwd           Imprimir diretório de trabalho
        lcd             Alterar diretório de trabalho local
        lls             Listar arquivos locais
        lpwd            Imprimir diretório de trabalho local
        ls              arquivos de lista
        mkdir           Fazer diretório
        mv              Mover a origem para o destino
        pwd             Print diretório de trabalho
        rm              Excluir o arquivo especificado
        rmdir           Remover diretório
        search          Pesquisar por arquivos
        upload          Carregar um arquivo ou diretório \n''')
        elif opc == 8 or opc == '08':
            print('''\033[7;36m COMANDOS PRINCIPAIS \033[m
             
        Comando                      Descrição
        -------                      -----------
        ?                            Menu de ajuda
        Background                   Backgrounds a sessão atual
        bgkill                       Elimina rastros deixados pelo payload\033[7;31m|EX: bgkill -i 1\033[m
        bglist                       Lista rastros deixados por você\033[7;31m|OBS: USADO JUNTO COM O bgkill\033[m1
        bgrun                        Executa um script meterpreter como um thread de segundo plano
        channel                      Exibe informações ou controla canais ativos
        close                        Fecha um canal
        disable_unicode_encoding     Desativa a codificação de sequências unicode
        enable_unicode_encoding      Ativa a codificação de sequências unicode
        exit                         Encerra a sessão do meterpreter
        get_timeouts                 Obtém os valores de tempo limite da sessão atual
        guid                         Obtenha a sessão GUID
        help                         menu Ajuda
        info                         Exibe informações sobre um módulo Post
        irb                          Solte no modo de script irb
        load                         Carrega uma ou mais extensões de meterpreter
        machine_id                   Obtém o ID do MSF da máquina anexada à sessão
        exit                         Encerrar a sessão do medidor
        read                         Lê dados de um canal
        resource                     Executar os comandos armazenados em um arquivo
        Execute                      Executa um script meterpreter ou um módulo Post
        sessions                     mudam rapidamente para outra sessão
        set_timeouts                 Define os valores de tempo limite da sessão atual
        sleep                        Force Meterpreter para ficar quieto e restabelecer a sessão.
        transport                    Alterar o mecanismo de transporte atual
        use                          o alias obsoleto para "load"
        uuid                         Obter o UUID para a sessão atual
        writes                       Grava dados em um canal \n''')
        elif opc == 9 or opc == '09':
            mts()
        elif opc == 99:
            menu()
        else:
            print('\033[31m OPÇÃO INVALIDA \033[m \n')
def termux():
    print('[01]COMANDOS BÁSICOS')
    time.sleep(0.5)
    print('[99]VOLTAR')
    z1 = int(input('\n trmx: \n'))
    if z1 == 1 or z1 == '01':
        print(''' \033[7;36m COMANDOS BÁSICOS DO TERMUX \033[m
        
        comandos                        descrição
        --------                        ---------
        apt update:                     Usado para baixar as informações do pacotes configurados.
        apt upgrade:                    É usado para instalar atualizações disponíveis de todos os pacotes. 
        ls:                             Usado para listar diretórios.
        termux-setup-storage:           Garante a permissão de leitura de arquivos.
        cd:                             Usado para navegar entre diretórios\033[7;31m|EX: cd downloads\033[m
        mv:                             Usado para mover aquivos\033[7;31m|EX: mv xerxes.c /$HOME\033[m
        rm:                             remove arquivos e diretórios\033[7;31m|EX: rm xerxes\033[m
        chmod:                          Comando que pode alterar permissões de acesso\033[7;31m|EX: chmod +x xerxes.c\033[m
        pwd:                            mostra o caminho completo do diretório em que você se encontra.
        cat:                            mostra o conteúdo de um arquivo binário ou texto\033[7;31m|EX: cat arquivo.txt\033[m
        cd.. :                          Volta ao diretório anterior.
        clear:                          limpa a tela do terminal.
        chmod 777:                      Dá permissão total ao arquivo\033[7;31m|EX: chmod 777 xerxes.c \033[m
        cp:                             Copia todo o conteúdo do diretório.
        kill:                           Encerra um ou mais processos em andamento.
        rm -rf:                         remove todos os arquivos e subdiretórios do diretório especificado.
        unzip:                          descompacta arquivos .zip\033[7;31m|EX: unzip ngrok.zip \033[m \n ''')
        termux()
    elif z1 == 99:
        menu()
    else:
        print('\033[31m OPÇÃO INVALIDA \033[m \n')
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
def xerxes():
    print('\n[01]COMANDOS')
    time.sleep(0.5)
    print('[02]INSTALAR')
    time.sleep(0.5)
    print('[99]VOLTAR')
    time.sleep(0.5)
    n3 = int(input('\n xrxs: \n'))
    if n3 == 1 or n3 == '01':
        print('\n(01):| cd xerxes')
        print('(02):| pkg install clang')
        print('(03):| clang xerxes.c -o xerxes')
        print('(04):| ./xerxes (\033[7;31m site ou ip \033[m)')
        xerxes()
    elif n3 == 2 or n3 == '02':
        xerxesin()
    elif n3 == 99:
        menu()
    else:
        print('\033[31m OPÇÃO INVALIDA \033[m \n')
def sql():
    print('[01]COMANDOS')
    time.sleep(0.5)
    print('[02]INSTALAR')
    time.sleep(0.5)
    print('[99]VOLTAR')
    time.sleep(0.5)
    n1 = int(input('\n sql: \n'))
    if n1 == 1 or n1 == '01':
        print('\n(01):|python2 sqlmap.py -u [\033[7;31m site sem parênteses \033[m] --dbs')
        print('\n(02):|python2 sqlmap.py -u [\033[7;31m site \033[m] --dbs -D [\033[7;31m dbs \033[m] --tables')
        print('\n(03):|python2 sqlmap.py -u [\033[7;31m site \033[m] --dbs -D [\033[7;31m dbs \033[m] -T [\033[7;31m tabela \033[m] --columns')
        print('\n(04):|python2 sqlmap.py -u [\033[7;31m site \033[m] --dbs -D [\033[7;31m dbs \033[m] -T [\033[7;31m tabela \033[m] -C [\033[7;31m coluna \033[m] -- dump')
        print('\n   \033[7;36m OBSERVAÇÃO: QUALQUER ERRO DE ESCRITA ALTERA DIRETAMENTE O RESULTADO! \033[m')
        print('   \033[7;36m OBSERVE ATENTAMENTE O SEU COMANDO ANTES DE EXECUTÁ-LO! \033[m \n')
        sql()
    elif n1 == 2 or n1 == '02':
        sqlmap()
    elif n1 == 99:
        menu()
    else:
        print('\033[31m OPÇÃO INVALIDA \033[m \n')
menu()
