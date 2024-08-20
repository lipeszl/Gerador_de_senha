import string
import random
import pyperclip
from tkinter import messagebox
from datetime import datetime

# Definições de conjuntos de caracteres
alfabeto_caps = string.ascii_uppercase
alfabeto_normal = string.ascii_lowercase
numeros = '1234567890'
simbolos = '[]{}()*;/,-_ç'

def criar_senha(qtd_caracteres, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
    combinar = ''

    # Adicionar caracteres de acordo com os botões selecionados
    if usar_maiusculas:
        combinar += alfabeto_caps
    if usar_minusculas:
        combinar += alfabeto_normal
    if usar_numeros:
        combinar += numeros
    if usar_simbolos:
        combinar += simbolos

    # Gera a senha com o número de caracteres especificado
    if combinar:
        senha = "".join(random.sample(combinar, qtd_caracteres))
        salvar_senha(senha) # Salva a senha gerada
        return senha
    else:
        return "Selecione uma opção!"

def copiar_senha(senha):
    pyperclip.copy(senha)
    messagebox.showinfo("sucesso", "A senha foi copiada")


def salvar_senha(senha):
    with open("senhas_geradas.txt", "a") as arquivo:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"{timestamp} - {senha}\n")
