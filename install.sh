#!/bin/bash

# Instalação de dependências
instalar_dependencias() {
    sudo apt-get install xdotool wmctrl
}

# Função principal
instalar_script() {
    # Obtém o diretório atual do script
    local script_dir=$(dirname "$0")

    # Adicionar o diretório ao PATH
    echo "export PATH=\$PATH:$script_dir/src" >> ~/.bashrc
    source ~/.bashrc

    # Criar um link simbólico em /usr/local/bin/
    ln -s "$script_dir/src/dg.py" /usr/local/bin/dg

    # Dar permissão de execução ao script Python
    chmod +x "$script_dir/src/dg.py"

    echo "Instalação concluída com sucesso!"
}

# Executar instalação de dependências
instalar_dependencias
# Executar a função principal
instalar_script
