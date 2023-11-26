#!/bin/bash

instalar_script() {
    
    # Caminho atual do diretório
    script_dir=$(dirname "$(readlink -f "$BASH_SOURCE")")

    # Adicionar o diretório ao PATH
    echo "export PATH=\$PATH:$script_dir/src" >> ~/.bashrc
    source ~/.bashrc

    # Criar um link simbólico em /usr/local/bin/
    sudo ln -s "$script_dir/src/dg.py" /usr/local/bin/dg

    # Dar permissão de execução ao script Python
    sudo chmod +x "$script_dir/src/dg.py"

    echo "Instalação concluída com sucesso!"
}

# Executar a função principal
instalar_script