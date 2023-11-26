#!/usr/bin/env python3

"""O shebang é uma linha especial que indica ao sistema operacional qual interpretador 
usar para executar o script. Para Python, o shebang geralmente é: #!/usr/bin/env python3"""

import sys
from funcs import *

try:
    # Obtendo argumento da linha de comando
    argumento = sys.argv[1]
    commands = {"help": help,
                "help_commands": help_commands,
                "print": screenshot,
                "code": vscode,
                "w": whereAmI,
                "dep": showDep,
                }
    if argumento in commands:
        commands[argumento]() 
    # Se o comando for "copy", ele irá executar a instrução depois de copy e copiar o resultado.
    elif len(sys.argv) > 1 and sys.argv[1] == "copy":
        # Não pega os argumentos 'dg' e 'copy'
        command_to_run = sys.argv[2:]
        copy(command_to_run)
    elif len(sys.argv) > 1 and sys.argv[1] == "todo":
        command_to_run = sys.argv[2:]
        todo(command_to_run)
    else:
        help()
except Exception as e:
    print(e)

"""
How to build in Linux Mint:

Passo 1: shebang.
No início do seu script Python (exe.py), adicione um shebang para 
indicar qual interpretador Python deve ser usado. Abra o script em um 
editor de texto e adicione a linha: #!/usr/bin/env python3

Passo 2: tornar o script executável.
No terminal, vá para o diretório onde o script está localizado e torne o 
script executável com o comando: chmod +x dg.py

Passo 3: adicionar ao PATH.
Se você quiser executar o script de qualquer lugar sem especificar o 
caminho completo, você pode adicionar o diretório ao seu PATH. Abra 
o seu arquivo de perfil (~/.bashrc ou ~/.zshrc) em um editor de 
texto e adicione a linha: export PATH=$PATH:/home/doug/dg-script/
Em seguida, recarregue o perfil: source ~/.bashrc

Passo 4: criar o link simbólico.
Finalmente, crie um link simbólico em um diretório que já está no 
seu PATH, como /usr/local/bin/: ln -s /home/doug/dg-script/src/dg.py /usr/local/bin/dg
"""


