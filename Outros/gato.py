import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def carregarImagemGato ():
    url_api = "https://api.thecatapi.com/v1/images/search"
    resposta = requests.get (url_api)

    if resposta.status_code == 200:
        dados = resposta.json ()
        url_imagem = dados[0]["url"]
        imagem_resposta = requests.get (url_imagem)
        imagem_bytes = Image.open (BytesIO (imagem_resposta.content))

        imagem_redimensionada = imagem_bytes.resize ((300, 300))
        imagem_tk = ImageTk.PhotoImage (imagem_redimensionada)

        rotulo_imagem.config (image=imagem_tk)
        rotulo_imagem.image = imagem_tk
        rotulo_info.config (text="Clique no botão para ver outro gato!")
    else:
        rotulo_info.config (text="Erro ao carregar a imagem.")

janela = tk.Tk ()
janela.title ("Imagem de Gato Aleatória")
janela.geometry ("320x400")

rotulo_info = tk.Label (janela, text="Clique no botão para carregar um gato 🐱")
rotulo_info.pack (pady=10)

rotulo_imagem = tk.Label (janela)
rotulo_imagem.pack ()

botao = tk.Button (janela, text="Novo Gato", command=carregarImagemGato)
botao.pack (pady=10)

janela.mainloop ()