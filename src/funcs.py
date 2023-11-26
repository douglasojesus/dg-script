import subprocess
import os
from datetime import datetime, date
from request import obter_dados_meteorologicos
from config import CHAVE_API_OPENWEATHERMAP


def showDep():
    print("""
    Python:
        subprocess, os, sys, datetime, request
    Shell:
        sudo apt-get install xdotool wmctrl
    API:
        src/funcs.whereAmI SUA_CHAVE_API https://openweathermap.org/api
    """)

def help():
    print("""Comandos executáveis:
    
    help: retorna lista de comandos executáveis;
    help_commands: mostra os comandos mais utilizados no terminal;
    print: seleciona área para screenshot e copia para Área de Transferência (minimiza terminal);
    code: abre diretório atual com Visual Studio Code;
    w: mostra diretório, tempo, data e temperatura em FSA atual;
    copy + command*: copia o resultado do comando para Área de Transferência e exibe no terminal;
          
    *command: precisa ser o comando completo, não atalho (por ex: 'dg copy ls -l', não 'dg copy ll')
    """)

def help_commands():
    print("""Navegação no Sistema de Arquivos:

    cd: Muda o diretório atual.
    ls: Lista os arquivos e diretórios no diretório atual.
    pwd: Mostra o caminho do diretório atual.
    find: Busca arquivo (find diretorio/inicio -name "nome_arquivo.txt").
    locate: Busca arquivo (locate "nome_arq.txt") em banco (para atualizar banco: sudo updatedb).
          
Manipulação de Arquivos e Diretórios:

    cp: Copia arquivos ou diretórios.
    mv: Move ou renomeia arquivos e diretórios.
    rm: Remove arquivos ou diretórios.
    mkdir: Cria um novo diretório.

Gerenciamento de Pacotes:

    apt: Ferramenta para gerenciar pacotes.
    sudo apt update: Atualiza a lista de pacotes disponíveis.
    sudo apt upgrade: Atualiza os pacotes instalados.
    sudo apt install nome_do_pacote: Instala um novo pacote.
    sudo apt remove nome_do_pacote: Remove um pacote.

Permissões e Propriedades de Arquivos:

    chmod: Modifica as permissões de arquivos.
    chown: Altera o proprietário de um arquivo.
    chgrp: Altera o grupo de um arquivo.

Consulta de Informações do Sistema:

    uname -a: Exibe informações do kernel.
    lsb_release -a: Exibe informações sobre a distribuição Linux.
    df -h: Mostra o espaço em disco disponível.

Rede:

    ifconfig ou ip addr: Exibe informações sobre interfaces de rede.
    ping: Testa a conectividade com um host.
    nslookup ou dig: Consulta informações de DNS.

Visualização de Arquivos de Texto:

    cat: Concatena e exibe o conteúdo de arquivos.
    more ou less: Permite visualizar grandes arquivos de texto.
    head e tail: Exibe as primeiras ou últimas linhas de um arquivo.

Edição de Texto no Terminal:

    nano, vim, ou emacs: Editores de texto no terminal.

Usuários e Grupos:

    sudo: Executa comandos com privilégios de superusuário.
    useradd: Adiciona um novo usuário.
    passwd: Define ou altera a senha de um usuário.
    groupadd: Adiciona um novo grupo.

Informações de Hardware:

    lscpu: Exibe informações sobre a CPU.
    lshw: Lista detalhes de hardware.
    free -m: Exibe informações sobre o uso da memória.

Para obter informações detalhadas sobre qualquer comando, 
você pode consultar o manual usando "man nome_do_comando". 
    """)

def screenshot():
    subprocess.run(["xdotool", "getactivewindow", "windowminimize"])
    #Para registrar print selecionando área e copiando para Área de Transferência
    resultado = subprocess.run(["gnome-screenshot", "-ac"], capture_output=True, text=True)
    #Se houver saída, usar resultado.stdout
    #resultado.returncode mostra se foi feito com sucesso (0) ou não
    os.system("wmctrl -a :ACTIVE:")
    if resultado.returncode == 0:
        print("dg answers you: screenshot realizado e copiado para área de transferência.")
    else:
        print("Houve erro no comando. Mensagem: ", resultado.returncode)
    
def vscode():
    # Obtém o caminho do diretório atual
    current_directory = os.getcwd()
    # Executa o Visual Studio Code no diretório atual
    subprocess.run(["flatpak", "run", "com.visualstudio.code", current_directory])

def whereAmI():
    current_directory = os.getcwd()
    current_time = datetime.now().time()
    current_time = current_time.strftime("%H:%M:%S")
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    # Lembre de colocar sua chave API aqui (Para criar: https://openweathermap.org/api)
    # Cuidado para não expor no GitHub hahaha
    SUA_CHAVE_API = CHAVE_API_OPENWEATHERMAP
    temperatura, sensacao_termica = obter_dados_meteorologicos('Feira de Santana', SUA_CHAVE_API)
    if temperatura is not None and sensacao_termica is not None:
        temp_data = f"{temperatura-273.15:.2f}°C - thermal sensation: {sensacao_termica-273.15:.2f}°C"
    else:
        temp_data = "Não foi possível obter os dados meteorológicos."

    print(f"""
    where are you now: {current_directory}
    what time is it: {current_time}
    what date is it: {today}
    what about the temperature in FSA: {temp_data}
""")
    
def copy(command):
    try:
        # Execute o processo e capture a saída
        resultado = subprocess.run(command, capture_output=True, text=True)
        print(resultado.stdout, end="")
        # Converta a saída para bytes
        output_bytes = resultado.stdout.encode("utf-8")
        # Usando o script xclip para copiar a saída do comando anterior (output) para input.
        subprocess.run(["xclip", "-selection", "clipboard"], input=output_bytes)
        print("dg answers you: saída do comando copiada para a área de transferência.")
    except subprocess.CalledProcessError as e:
        print(f"dg answers you: erro ao executar o comando: {e}")

