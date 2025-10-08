from tkinter import *
from PIL import Image, ImageTk
from dotenv import load_dotenv
import requests
import os

load_dotenv()

# ======= CORES =======
cor1 = "#ffffff"     # branca 
cor2 = "#333333"     # preta
fundo_day = "#21afbc"    # azul claro (dia)
fundo_night = "#0f2b4b"  # azul escuro (noite)

# ======= JANELA PRINCIPAL =======
janela = Tk()
janela.title("Clima")
janela.geometry('360x420')    
janela.configure(bg=fundo_day)
janela.resizable(False, False)

# ======= FRAME SUPERIOR =======
frame_top = Frame(janela, width=360, height=70, bg=fundo_day)
frame_top.pack(side=TOP, fill=X)

# ======= FRAME CORPO =======
frame_corpo = Frame(janela, width=360, height=350, bg=fundo_day)
frame_corpo.pack(fill=BOTH, expand=True)

# ======= FUNÇÃO PRINCIPAL =======
def informacao(event=None):
    chave_api = os.getenv("CHAVE_API_WEATHER")
    if not chave_api:
        raise RuntimeError("API key não encontrada ou não informada.")
    cidade = e_local.get().strip()
    if not cidade:
        l_cidade.config(text="Digite uma cidade")
        return

    api_link = f"http://api.weatherapi.com/v1/current.json?key={chave_api}&lang=pt&q={cidade}"

    try:
        r = requests.get(api_link, timeout=4)
        r.raise_for_status()
        dados = r.json()

        # ======= DADOS =======
        nome = dados['location']['name']
        pais = dados['location']['country']
        horario = dados['location']['localtime']
        temperatura = dados['current']['temp_c']
        sensacao = dados['current']['feelslike_c']
        vento = dados['current']['wind_kph']
        descricao = dados['current']['condition']['text']
        is_day = dados['current']['is_day']

        # ======= TROCA DE COR DE FUNDO =======
        bg_color = fundo_day if is_day == 1 else fundo_night
        frame_corpo.configure(bg=bg_color)
        janela.configure(bg=bg_color)

        # ======= ATUALIZA LABELS =======
        l_cidade.config(text=f"{nome}, {pais}", bg=bg_color)
        l_data.config(text=horario, bg=bg_color)
        l_temperatura.config(text=f"{int(temperatura)}°C", bg=bg_color)
        l_sensacao.config(text=f"Sensação Térmica: {sensacao}°C", bg=bg_color)
        l_velocidade_vento.config(text=f"Vento: {vento} Km/h", bg=bg_color)
        l_descricao_do_dia.config(text=descricao, bg=bg_color, wraplength=160, justify=LEFT)

        # ======= HORA =======
        try:
            hora = int(horario.split(" ")[1].split(":")[0])
        except:
            hora = 12

        descricao_lower = descricao.lower()

        # ======= ESCOLHA DE IMAGEM =======
        if "neve" in descricao_lower:
            imagem_path = "images/snow.png"
        elif "tempestade" in descricao_lower or "tormenta" in descricao_lower:
            imagem_path = "images/storm.png"
        elif "chuva" in descricao_lower:
            imagem_path = "images/light_rain.png"
        elif "nublado" in descricao_lower or "cloud" in descricao_lower:
            imagem_path = "images/cloudy.png"
        elif is_day == 0:
            imagem_path = "images/light_night.png"
        elif 17 <= hora < 19:
            imagem_path = "images/sunset.png"
        elif "sol" in descricao_lower and is_day == 1:
            imagem_path = "images/sun.png"
        else:
            imagem_path = "images/very_cloudy.png"

        # ======= ATUALIZA ÍCONE =======
        l_icon.config(bg=bg_color)
        if os.path.exists(imagem_path):
            imagem_nova = Image.open(imagem_path)
            imagem_nova = imagem_nova.resize((110, 110), Image.Resampling.LANCZOS)
            imagem_nova = ImageTk.PhotoImage(imagem_nova)
            l_icon.config(image=imagem_nova)
            l_icon.image = imagem_nova
        else:
            l_icon.config(image='', text='[sem imagem]', fg=cor1, bg=bg_color)

    except Exception as e:
        l_cidade.config(text="Erro ao obter dados", bg=fundo_day)
        print("Erro:", e)

# ======= INPUT E BOTÃO =======
e_local = Entry(frame_top, width=22, font=("Arial", 14), relief='solid', justify='left')
e_local.place(x=15, y=18)
e_local.bind('<Return>', informacao)

b_local = Button(frame_top, command=informacao, text='Ver Clima',
                 bg=cor1, fg=cor2, font=('Segoe UI Semibold', 10),
                 relief='raised', overrelief=RIDGE)
b_local.place(x=270, y=18)

# ======= LABELS INICIAIS =======
l_cidade = Label(frame_corpo, text='Cidade, País', bg=fundo_day, fg=cor1, font=('Segoe UI', 13, 'bold'))
l_cidade.place(x=10, y=8)

l_data = Label(frame_corpo, text='--/--/---- | --:--', bg=fundo_day, fg=cor1, font=('Segoe UI', 11))
l_data.place(x=10, y=34)

l_temperatura = Label(frame_corpo, text='--°C', bg=fundo_day, fg=cor1, font=('Poppins', 42, 'bold'))
l_temperatura.place(x=10, y=70)

l_descricao_do_dia = Label(frame_corpo, text='---', bg=fundo_day, fg=cor1, font=('Nunito Sans', 12, 'bold'))
l_descricao_do_dia.place(x=190, y=170, width=160, height=40)

l_velocidade_vento = Label(frame_corpo, text='Vento: -- Km/h', bg=fundo_day, fg=cor1, font=('Segoe UI', 12, 'bold'))
l_velocidade_vento.place(x=10, y=190)

l_sensacao = Label(frame_corpo, text='Sensação Térmica: --°C', bg=fundo_day, fg=cor1, font=('Segoe UI', 11, 'bold'))
l_sensacao.place(x=10, y=250)

# ======= ÍCONE PADRÃO =======
imagem_padrao = Image.open('images/sun.png')
imagem_padrao = imagem_padrao.resize((110, 110), Image.Resampling.LANCZOS)
imagem_padrao = ImageTk.PhotoImage(imagem_padrao)
l_icon = Label(frame_corpo, image=imagem_padrao, bg=fundo_day)
l_icon.place(x=230, y=50)

# ======= LOOP PRINCIPAL =======
janela.mainloop()
