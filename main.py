from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from logica import *

Cor_Preta = "#444466"  # Preto
Cor_Branca = "#feffff"  # Branco
Cor_Vermelha = "#f05a43"  # Vermelho

janela = Tk()
janela.title('')
janela.geometry('350x380')
janela.configure(bg=Cor_Branca)

# Frame das telas divididos
frame_cima = Frame(janela, width=280, height=50, bg=Cor_Branca, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=280, height=310, bg=Cor_Branca, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Trabalho no frame de cima
img = Image.open('cachorrosantos.jpg')
img = img.resize((30, 30), Image.Resampling.NEAREST)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=Cor_Branca)
app_logo.place(x=0, y=0)

app_nome = Label(frame_cima, text='Gerador de Senha', height=1, width=20, padx=0, relief='flat', anchor='nw', font=('Ivy 16 bold'), bg=Cor_Branca, fg=Cor_Preta)
app_nome.place(x=35, y=0)

app_linha = Label(frame_cima, text='', height=1, width=295, padx=0, relief='flat', anchor='nw', font=('Ivy 1 bold'), bg=Cor_Vermelha, fg=Cor_Preta)
app_linha.place(x=0, y=35)

# Trabalho no frame de baixo

app_senha = Label(frame_baixo, text='- - - -', height=2, width=28, padx=0, relief='solid', anchor='center', font=('Ivy 12 bold'), bg=Cor_Branca, fg=Cor_Preta)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label(frame_baixo, text='Numero total de caracteres para senha', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=Cor_Branca, fg=Cor_Preta)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=3, pady=1)

# Variável de quantos números a senha vai ter
var = IntVar()
var.set(0)
spin = Spinbox(frame_baixo, from_=0, to=55, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8)

# Mostrar os caracteres

frame_caracteres = Frame(frame_baixo, width=295, height=210, bg=Cor_Branca, pady=0, padx=0, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

# Estado dos botões

estado_1 = BooleanVar()
estado_2 = BooleanVar()
estado_3 = BooleanVar()
estado_4 = BooleanVar()

# Área do botão das letras maiusculas
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, relief='flat', bg=Cor_Branca)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Letras maiusculas', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=Cor_Branca, fg=Cor_Preta)
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=5)

# Área do botão das letras minusculas
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2, relief='flat', bg=Cor_Branca)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Letras minusculas', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=Cor_Branca, fg=Cor_Preta)
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=5)

# Área do botão dos números
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3, relief='flat', bg=Cor_Branca)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Números', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=Cor_Branca, fg=Cor_Preta)
app_info.grid(row=2, column=1, sticky=NW, padx=2, pady=5)

# Área do botão dos símbolos
check_4 = Checkbutton(frame_caracteres, width=1, var=estado_4, relief='flat', bg=Cor_Branca)
check_4.grid(row=3, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Simbolos', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=Cor_Branca, fg=Cor_Preta)
app_info.grid(row=3, column=1, sticky=NW, padx=2, pady=5)

# Função para gerar senha ao clicar no botão
def gerar_senha():
    qtd_caracteres = var.get()
    usar_maiusculas = estado_1.get()
    usar_minusculas = estado_2.get()
    usar_numeros = estado_3.get()
    usar_simbolos = estado_4.get()
    
    senha = criar_senha(qtd_caracteres, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos)
    app_senha.config(text=senha)


# Botão de gerar senha
botao_gerar_senha = Button(frame_caracteres, text='Gerar Senha', width=34, height=1, relief='flat', overrelief='solid', anchor='center', font=('Ivy 10 bold'), bg=Cor_Vermelha, fg=Cor_Branca, command=gerar_senha)
botao_gerar_senha.grid(row=5, column=0, sticky=NSEW, padx=5, pady=11, columnspan=5)

# Botão de copiar senha
botao_copiar_senha = Button(frame_baixo, text='Copiar', width=7, height=2, relief='raised', overrelief='solid', anchor='center', font=('Ivy 10 bold'), bg=Cor_Vermelha, fg=Cor_Branca, command=lambda: copiar_senha(app_senha.cget("text")))
botao_copiar_senha.grid(row=0, column=1, sticky=NW, padx=5, pady=10, columnspan=1)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

janela.mainloop()