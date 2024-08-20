# Gerador de Senhas com Tkinter

Este projeto é um gerador de senhas simples, construído usando Python, Tkinter e PIL (Pillow). O gerador de senhas permite que os usuários criem senhas com um número personalizado de caracteres e diferentes conjuntos de caracteres (letras maiúsculas, letras minúsculas, números e símbolos). As senhas geradas são automaticamente salvas em um arquivo `.txt` com um timestamp e podem ser copiadas para a área de transferência.

## Funcionalidades

- Geração de senhas com até 35 caracteres.
- Opções para incluir letras maiúsculas, letras minúsculas, números e símbolos.
- Cópia da senha gerada para a área de transferência.
- Salvamento automático das senhas geradas em um arquivo `.txt`.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- Python 3.x
- Tkinter (geralmente incluído com o Python)
- PIL (Pillow) para manipulação de imagens
- `pyperclip` para copiar texto para a área de transferência

Você pode instalar as bibliotecas necessárias usando o pip:


pip install pillow pyperclip
Estrutura do Projeto
main.py: Contém a interface gráfica do usuário (GUI) construída com Tkinter, incluindo os botões para gerar e copiar senhas.
logica.py: Contém a lógica para criar senhas e salvar as senhas geradas em um arquivo .txt.
senhas_geradas.txt: Arquivo onde as senhas geradas são salvas com um timestamp.

##Uso

Execute o arquivo main.py para iniciar a interface gráfica:

Gerar Senha:

Selecione as opções desejadas para incluir letras maiúsculas, letras minúsculas, números e símbolos.
Defina o número de caracteres para a senha.
Clique no botão "Gerar Senha" para criar uma nova senha.

Copiar Senha:

Clique no botão "Copiar" para copiar a senha gerada para a área de transferência.
Ver Senhas Salvas:

As senhas geradas são salvas automaticamente em senhas_geradas.txt com um timestamp.
