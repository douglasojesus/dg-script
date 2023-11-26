#!/bin/bash

# Função principal
instalar_script() {
    # Obtém o diretório atual do script
    local script_dir=$(dirname "$0")

    # Adicionar o diretório ao PATH
    #echo "export PATH=\$PATH:$script_dir/src" >> ~/.bashrc
    export PATH=$PATH:$script_dir/src
    #source ~/.bashrc

    # Criar um link simbólico em /usr/local/bin/
    #ln -s "$script_dir/src/dg.py" /usr/local/bin/dg
    rm ~/.local/bin/dg
    ln -s "$script_dir/src/dg.py" ~/.local/bin/dg

    # Dar permissão de execução ao script Python
    chmod +x "$script_dir/src/dg.py"

    echo "Instalação concluída com sucesso!"
}

# Executar a função principal
instalar_script
