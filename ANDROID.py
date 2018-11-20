#Copyright (C) 2018

import time

print('''\033[32m
    _      _  _ _ _ _____  _ _ _   _ _   _ _   _ _   _ _ _ _____  _ _ _   _ _
   | \    / ||        |   |       |   | |   | |   | |        |   |       |   |
   |  \  /  ||_ _ _   |   |_ _ _  |_ _| |_ _| |_ _| |_ _ _   |   |_ _ _  |_ _|
   |   \/   ||        |   |       | \   |     | \   |        |   |       | \ 
   |        ||_ _ _   |   |_ _ _  |  \  |     |  \  |_ _ _   |   |_ _ _  |  \ 
                         
                        \033[35m !!!MADE SIXX66 BY GASPAR!!! \033[0m''')
print('\n CARREGANDO...')
time.sleep(2)
time.sleep(0)



while True:
    print('''\033[36m 
    [1]COMANDOS DO ANDROID
    [2]COMANDOS DE AUDIO
    [3]COMANDOS DA WEBCAM
    [4]COMANDOS DA INTERFACE
    [5]COMANDOS DO SISTEMA
    [6]COMANDOS DE REDE
    [7]COMANDOS DO SISTEMA DE ARQUIVOS
    [8]COMANDOS PRINCIPAIS
    [9]SAIR''')
    opc = int(input('\033[31m>>>: '))
    if opc == 1:
        print('''Comandos do Android
================

    Comando          Descrição
    -------          -----------
    activity_start    Inicie uma atividade do Android a partir de uma string Uri
    check_root        Verifique se o dispositivo está enraizado
    dump_calllog      Obter registro de chamadas
    dump_contacts     Obter lista de contatos
    dump_sms          Obter mensagens sms
    geolocate         Obtenha o lat atual usando a geolocalizaçãoreOcultar o ícone do aplicativo no iniciador
    interval_collect  Gerenciar recursos de coleta de intervalo
    send_sms          Envia SMS da sessão de destino
    set_audio_mode    Definir o modo de campainha
    sqlite_query      Consultar um banco de dados SQLite do armazenamento
    wakelock          Ativar / Desativar o Wakelock
    wlan_geolocate    Obtém o lat atual usando informações de WLAN''')
    elif opc == 2:
        print('''Comandos de Saída de Áudio
=============================

    Comando            Descrição
    -------            -----------
    reproduzir         reproduzir um arquivo de áudio no sistema de destino, nada escrito no disco
''')
    elif opc == 3:
        print('''comandos da webcam
=======================

    Comando         Descrição
    -------         -----------
    record_mic      Grava áudio do microfone padrão por X segundos
    webcam_chat     Iniciar um bate-papo por vídeo
    webcam_list     Lista de webcams
    webcam_snap     Tire um instantâneo da webcam especificada
    webcam_stream   Reproduz um fluxo de vídeo da webcam especificada
''')
    elif opc == 4:
        print('''Comandos da interface do usuário
===============================

    Comando              Descrição
    -------              -----------
    screenshot      Capture uma captura de tela da área de trabalho interativa 
''')
    elif opc == 5:
        print(''' Comandos do sistema
=======================

    Comando           Descrição
    -------           -----------
    execute           Execute um comando
    getuid            Obter o usuário que o servidor está executando como
    localtime         Exibe a data e hora locais do sistema de destino
    pgrep             Filtrar processos por nome
    ps                Processos em execução da lista
    shell             Drop into a shell de comando do sistema
    sysinfo           Obtém informações sobre o sistema remoto, como SO
''')
    elif opc == 6:
        print('''Comandos de Rede
===========================

    Comando                Descrição
    -------                -----------
    ifconfig               interfaces de exibição ifconfig
    ipconfig               interfaces de exibição ipconfig
    portfwd                Encaminhar uma porta local para um serviço remoto
    route                  Visualizar e modificar a tabela de roteamento
''')
    elif opc == 7:
        print('''Comandos do sistema de arquivos
============================

    Comando         Descrição
    -------         -----------
    cat             Leia o conteúdo de um arquivo na tela
    cd              Alterar diretório
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
    upload          Carregar um arquivo ou diretório
''')
    elif opc == 8:
        print('''' Comando                      Descrição
    -------                      -----------
    ?                            Menu de ajuda
    Background                   Backgrounds a sessão atual
    bgkill                       mata um script de medidor de antecedentes
    bglist                       Lists executando scripts de plano de fundo
    bgrun                        Executa um script meterpreter como um thread de segundo plano
    channel                      Exibe informações ou controla canais ativos
    close                        Fecha um canal
    disable_unicode_encoding     Desativa a codificação de sequências unicode
    enable_unicode_encoding      Ativa a codificação de sequências unicode
    exit                         Encerra a sessão do medidor
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
    writes                       Grava dados em um canal''')
    elif opc == 9:
        break
