import tkinter
from tkinter import *
from tkinter import ttk

#importando pillow
from PIL import Image, ImageTk

import requests
import datetime
import json

####################### CORES #####################
cor0 = "#444466" #PRETO
cor1 = "#feffff" #BRANCO
cor2 = "#6f9fbd" #AZUL

fundo_dia = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb86d"
fundo = fundo_dia

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)


#Criando os frames
frame_top = Frame(janela, width=320, height=50, bg=cor1, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')


# Funçao que retorna as informações
def informacao():
    chave_api = '3c1c80103ca742ce9a7151348250610'
    cidade = e_local.get()
    api_link = f"http://api.weatherapi.com/v1/current.json?key={chave_api}&lang=pt&q={cidade}"

    #-----fazendo a chamada da APi-----#
    r = requests.get(api_link)

    #-----convertendo os dados da variavel r em dicionario  (JSON) -----#
    dados = r.json()
    

    #-----Obtendo Pais, Zona e horário-----#
    info_pais = (
        dados['location']['name'],
        dados['location']['region'],
        dados['location']['country'],
        dados['location']['tz_id'],
        dados['location']['localtime']
    )


    #------Tempo-----#
    tempo = (
        dados['current']['temp_c'],
        dados['current']['condition']['text'],  # precisa acessar o texto dentro do dict 'condition'
        dados['current']['wind_kph'],
        dados['current']['pressure_mb'],
        dados['current']['humidity'],
        dados['current']['cloud'],
        dados['current']['feelslike_c']
    )


# Passando as informações para as Labels
  



#Configurando o frame top
e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)

b_local = Button(frame_top, command=informacao, text='Ver Clima', bg=cor1, fg=cor2, font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE)
b_local.place(x=250, y=10)

#Configurando frame corpo
l_cidade = Label(frame_corpo, text='',anchor='center', bg=fundo, fg=cor1, font=("Arial 13 bold"),)
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text='06-10-2025 | 10:39:00 AM',anchor='center', bg=fundo, fg=cor1, font=("Arial 11 bold"),)
l_data.place(x=10, y=40)

l_temperatura = Label(frame_corpo, text='84',anchor='center', bg=fundo, fg=cor1, font=("Arial 40"),)
l_temperatura.place(x=10, y=100)

l_temperatura_simbolo = Label(frame_corpo, text='°C',anchor='center', bg=fundo, fg=cor1, font=("Arial 40 bold"),)
l_temperatura_simbolo.place(x=70, y=100)

l_sensacao = Label(frame_corpo, text='Sensação Térmica: 45',anchor='center', bg=fundo, fg=cor1, font=("Arial 11 bold"),)
l_sensacao.place(x=10, y=184)

l_velocidade_vento = Label(frame_corpo, text='Velocidade do Vento: 40 Km/h' ,anchor='center', bg=fundo, fg=cor1, font=("Arial 11 bold"),)
l_velocidade_vento.place(x=10, y=230)

imagem = Image.open('images/sol_dia.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_corpo, image=imagem, bg=fundo)
l_icon.place(x=167, y=60)  

l_descricao_do_dia = Label(frame_corpo, text='Nublado' ,anchor='center', bg=fundo, fg=cor1, font=("Arial 11 bold"),)
l_descricao_do_dia.place(x=200, y=190)



janela.mainloop()