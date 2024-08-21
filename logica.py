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
        if qtd_caracteres > len(combinar):
            return "Número de caracteres maior que a combinação disponível!"
        senha = ''.join(random.choices(combinar, k=qtd_caracteres))
        return senha
    else:
        return "Selecione uma opção!"
    
# Função para gerar o popup quando se copia a senha

def copiar_senha(senha):
    pyperclip.copy(senha)
    messagebox.showinfo("Sucesso", "A senha foi copiada")
        
# Função para salvar a senha

def salvar_senha(senha):
    with open("senhas_geradas.txt", "a") as arquivo:
        timestamp = datetime.now().strftime("%d-%m-%Y // %H:%M:%S")
        arquivo.write(f"{timestamp} - A senha gerada foi: {senha}\n")