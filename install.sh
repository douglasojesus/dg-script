#!/bin/bash

# Solicitar ao usuário instalar dependências manualmente antes de executar o script
echo "Certifique-se de instalar as dependências manualmente antes de executar o script:"
echo "sudo apt-get install xdotool wmctrl"
read -p "Pressione Enter para continuar..."

# Função para mover o diretório
mover_diretorio() {
    local origem="$1"
    local destino="$2"

    mv "$origem" "$destino"
}

# Função principal
instalar_script() {
    # Obtém o diretório atual do script
    local script_dir=$(dirname "$0")

    # Solicitar ao usuário o nome do usuário
    echo "Digite seu nome de usuário: "
    read nome_do_usuario

    # Definir a pasta home e o caminho do diretório do script
    local pasta_home="/home/$nome_do_usuario"
    local novo_caminho="$pasta_home/$script_dir/src"

    # Mover o diretório atual para o novo caminho
    mover_diretorio "$script_dir" "$pasta_home"

    # Adicionar o diretório ao PATH
    echo "export PATH=\$PATH:$novo_caminho/src" >> ~/.bashrc
    source ~/.bashrc

    # Criar um link simbólico em /usr/local/bin/
    ln -s "$novo_caminho/src/exe.py" /usr/local/bin/exe

    # Dar permissão de execução ao script Python
    chmod +x "$novo_caminho/src/exe.py"

    echo "Instalação concluída com sucesso!"
}

# Executar a função principal
instalar_script
