# DG-Script

Bem-vindo ao DG-Script, meu script pessoal em Bash! 🚀

Este script em Bash é uma ferramenta versátil projetada para simplificar várias tarefas por meio de um conjunto de funções personalizadas. Seja gerenciando arquivos, automatizando processos ou aprimorando meu fluxo de trabalho, este script tem como objetivo simplificar e aprimorar minha experiência no terminal.

Comandos atuais (seguidos do 'dg'):

- help: retorna lista de comandos executáveis;
- help_commands: mostra os comandos mais utilizados no terminal;
- print: seleciona área para screenshot e copia para Área de Transferência (minimiza terminal);
- code*: abre diretório atual com Visual Studio Code;
- w: mostra diretório, tempo, data e temperatura em FSA atual;
- copy + command**: copia o resultado do comando para Área de Transferência e exibe no terminal;

*executa através do flatpak (flatpak run com.visualstudio.code);     
**command: precisa ser o comando completo, não atalho (por ex: 'dg copy ls -l', não 'dg copy ll').

Para o comando "dg w", é necessário que você configure sua chave API no arquivo dg-script/src/funcs na função whereAmI() (Para criar: https://openweathermap.org/api).

## Como Rodar

Siga estes simples passos para começar a usar o DG-Script:

### 1. Instale as dependências

$ sudo apt-get install xdotool wmctrl gnome-screenshot xclip

### 2. Clone o repositório

$ git clone https://github.com/douglasojesus/dg-script

### 3. Torne o script "install.sh" executável

$ cd dg-script

$ chmod +x install.sh

### 4. Execute o script dentro do diretório

$ source install.sh

### 5. Teste o script

$ dg help
