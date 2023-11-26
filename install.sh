#!/bin/bash

# Obtém o diretório atual do script
script_dir=$(dirname "$0")

# Solicitar ao usuário o nome do usuário
echo "Digite seu nome de usuário: "
read nome_do_usuario

# Definir a pasta home e o caminho do diretório do script
pasta_home="/home/$nome_do_usuario"
novo_caminho="$pasta_home/$script_dir"

# Move o diretório atual para o novo caminho
mv "$script_dir" "$pasta_home"

# Adicionar o diretório ao PATH
echo "export PATH=\$PATH:$novo_caminho" >> ~/.bashrc

source ~/.bashrc

# Criar um link simbólico em /usr/local/bin/
ln -s "$novo_caminho/exe.py" /usr/local/bin/exe

# Dar permissão de execução ao script Python
chmod +x "$novo_caminho/exe.py"

echo "Instalação concluída com sucesso!"
